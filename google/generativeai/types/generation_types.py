# -*- coding: utf-8 -*-
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import annotations

import collections
import contextlib
import sys
from collections.abc import Iterable, AsyncIterable, Mapping
import dataclasses
import itertools
import json
import sys
import textwrap
from typing import Union, Any
from typing_extensions import TypedDict
import types

import google.protobuf.json_format
import google.api_core.exceptions

from google.ai import generativelanguage as glm
from google.generativeai import string_utils
from google.generativeai.types import content_types
from google.generativeai.responder import _rename_schema_fields

__all__ = [
    "AsyncGenerateContentResponse",
    "BlockedPromptException",
    "StopCandidateException",
    "IncompleteIterationError",
    "BrokenResponseError",
    "GenerationConfigDict",
    "GenerationConfigType",
    "GenerationConfig",
    "GenerateContentResponse",
]

if sys.version_info < (3, 10):

    def aiter(obj):
        return obj.__aiter__()

    async def anext(obj, default=None):
        try:
            return await obj.__anext__()
        except StopAsyncIteration:
            if default is not None:
                return default
            else:
                raise


class BlockedPromptException(Exception):
    pass


class StopCandidateException(Exception):
    pass


class IncompleteIterationError(Exception):
    pass


class BrokenResponseError(Exception):
    pass


class GenerationConfigDict(TypedDict, total=False):
    # TODO(markdaoust): Python 3.11+ use `NotRequired`, ref: https://peps.python.org/pep-0655/
    candidate_count: int
    stop_sequences: Iterable[str]
    max_output_tokens: int
    temperature: float
    response_mime_type: str
    response_schema: glm.Schema | Mapping[str, Any]  # fmt: off


@dataclasses.dataclass
class GenerationConfig:
    """A simple dataclass used to configure the generation parameters of `GenerativeModel.generate_content`.

    Attributes:
        candidate_count:
            Number of generated responses to return.
        stop_sequences:
            The set of character sequences (up
            to 5) that will stop output generation. If
            specified, the API will stop at the first
            appearance of a stop sequence. The stop sequence
            will not be included as part of the response.
        max_output_tokens:
            The maximum number of tokens to include in a
            candidate.

            If unset, this will default to output_token_limit specified
            in the model's specification.
        temperature:
            Controls the randomness of the output. Note: The
            default value varies by model, see the `Model.temperature`
            attribute of the `Model` returned the `genai.get_model`
            function.

            Values can range from [0.0,1.0], inclusive. A value closer
            to 1.0 will produce responses that are more varied and
            creative, while a value closer to 0.0 will typically result
            in more straightforward responses from the model.
        top_p:
            Optional. The maximum cumulative probability of tokens to
            consider when sampling.

            The model uses combined Top-k and nucleus sampling.

            Tokens are sorted based on their assigned probabilities so
            that only the most likely tokens are considered. Top-k
            sampling directly limits the maximum number of tokens to
            consider, while Nucleus sampling limits number of tokens
            based on the cumulative probability.

            Note: The default value varies by model, see the
            `Model.top_p` attribute of the `Model` returned the
            `genai.get_model` function.

        top_k (int):
            Optional. The maximum number of tokens to consider when
            sampling.

            The model uses combined Top-k and nucleus sampling.

            Top-k sampling considers the set of `top_k` most probable
            tokens. Defaults to 40.

            Note: The default value varies by model, see the
            `Model.top_k` attribute of the `Model` returned the
            `genai.get_model` function.

        response_mime_type:
            Optional. Output response mimetype of the generated candidate text.

            Supported mimetype:
                `text/plain`: (default) Text output.
                `application/json`: JSON response in the candidates.

        response_schema:
            Optional. Specifies the format of the JSON requested if response_mime_type is
            `application/json`.
    """

    candidate_count: int | None = None
    stop_sequences: Iterable[str] | None = None
    max_output_tokens: int | None = None
    temperature: float | None = None
    top_p: float | None = None
    top_k: int | None = None
    response_mime_type: str | None = None
    response_schema: glm.Schema | Mapping[str, Any] | None = None


GenerationConfigType = Union[glm.GenerationConfig, GenerationConfigDict, GenerationConfig]


def _normalize_schema(generation_config):
    # Convert response_schema to glm.Schema for request
    response_schema = generation_config.get("response_schema", None)
    if response_schema is None:
        return

    if isinstance(response_schema, glm.Schema):
        return

    if isinstance(response_schema, type):
        response_schema = content_types._schema_for_class(response_schema)
    elif isinstance(response_schema, types.GenericAlias):
        if not str(response_schema).startswith("list["):
            raise ValueError(
                f"Could not understand {response_schema}, expected: `int`, `float`, `str`, `bool`, "
                "`typing_extensions.TypedDict`, `dataclass`, or `list[...]`"
            )
        response_schema = content_types._schema_for_class(response_schema)

    response_schema = _rename_schema_fields(response_schema)
    generation_config["response_schema"] = glm.Schema(response_schema)


def to_generation_config_dict(generation_config: GenerationConfigType):
    if generation_config is None:
        return {}
    elif isinstance(generation_config, glm.GenerationConfig):
        schema = generation_config.response_schema
        generation_config = type(generation_config).to_dict(
            generation_config
        )  # pytype: disable=attribute-error
        generation_config["response_schema"] = schema
        return generation_config
    elif isinstance(generation_config, GenerationConfig):
        generation_config = dataclasses.asdict(generation_config)
        _normalize_schema(generation_config)
        return {key: value for key, value in generation_config.items() if value is not None}
    elif hasattr(generation_config, "keys"):
        generation_config = dict(generation_config)
        _normalize_schema(generation_config)
        return generation_config
    else:
        raise TypeError(
            "Did not understand `generation_config`, expected a `dict` or"
            f" `GenerationConfig`\nGot type: {type(generation_config)}\nValue:"
            f" {generation_config}"
        )


def _join_citation_metadatas(
    citation_metadatas: Iterable[glm.CitationMetadata],
):
    citation_metadatas = list(citation_metadatas)
    return citation_metadatas[-1]


def _join_safety_ratings_lists(
    safety_ratings_lists: Iterable[list[glm.SafetyRating]],
):
    ratings = {}
    blocked = collections.defaultdict(list)

    for safety_ratings_list in safety_ratings_lists:
        for rating in safety_ratings_list:
            ratings[rating.category] = rating.probability
            blocked[rating.category].append(rating.blocked)

    blocked = {category: any(blocked) for category, blocked in blocked.items()}

    safety_list = []
    for (category, probability), blocked in zip(ratings.items(), blocked.values()):
        safety_list.append(
            glm.SafetyRating(category=category, probability=probability, blocked=blocked)
        )

    return safety_list


def _join_contents(contents: Iterable[glm.Content]):
    contents = tuple(contents)
    roles = [c.role for c in contents if c.role]
    if roles:
        role = roles[0]
    else:
        role = ""

    parts = []
    for content in contents:
        parts.extend(content.parts)

    merged_parts = [parts.pop(0)]
    for part in parts:
        if not merged_parts[-1].text:
            merged_parts.append(part)
            continue

        if not part.text:
            merged_parts.append(part)
            continue

        merged_part = glm.Part(merged_parts[-1])
        merged_part.text += part.text
        merged_parts[-1] = merged_part

    return glm.Content(
        role=role,
        parts=merged_parts,
    )


def _join_candidates(candidates: Iterable[glm.Candidate]):
    candidates = tuple(candidates)

    index = candidates[0].index  # These should all be the same.

    return glm.Candidate(
        index=index,
        content=_join_contents([c.content for c in candidates]),
        finish_reason=candidates[-1].finish_reason,
        safety_ratings=_join_safety_ratings_lists([c.safety_ratings for c in candidates]),
        citation_metadata=_join_citation_metadatas([c.citation_metadata for c in candidates]),
        token_count=candidates[-1].token_count,
    )


def _join_candidate_lists(candidate_lists: Iterable[list[glm.Candidate]]):
    # Assuming that is a candidate ends, it is no longer returned in the list of
    # candidates and that's why candidates have an index
    candidates = collections.defaultdict(list)
    for candidate_list in candidate_lists:
        for candidate in candidate_list:
            candidates[candidate.index].append(candidate)

    new_candidates = []
    for index, candidate_parts in sorted(candidates.items()):
        new_candidates.append(_join_candidates(candidate_parts))

    return new_candidates


def _join_prompt_feedbacks(
    prompt_feedbacks: Iterable[glm.GenerateContentResponse.PromptFeedback],
):
    # Always return the first prompt feedback.
    return next(iter(prompt_feedbacks))


def _join_chunks(chunks: Iterable[glm.GenerateContentResponse]):
    chunks = tuple(chunks)
    return glm.GenerateContentResponse(
        candidates=_join_candidate_lists(c.candidates for c in chunks),
        prompt_feedback=_join_prompt_feedbacks(c.prompt_feedback for c in chunks),
        usage_metadata=chunks[-1].usage_metadata,
    )


_INCOMPLETE_ITERATION_MESSAGE = """\
Please let the response complete iteration before accessing the final accumulated
attributes (or call `response.resolve()`)"""


class BaseGenerateContentResponse:
    def __init__(
        self,
        done: bool,
        iterator: (
            None
            | Iterable[glm.GenerateContentResponse]
            | AsyncIterable[glm.GenerateContentResponse]
        ),
        result: glm.GenerateContentResponse,
        chunks: Iterable[glm.GenerateContentResponse] | None = None,
    ):
        self._done = done
        self._iterator = iterator
        self._result = result
        if chunks is None:
            self._chunks = [result]
        else:
            self._chunks = list(chunks)
        if result.prompt_feedback.block_reason:
            self._error = BlockedPromptException(result)
        else:
            self._error = None

    @property
    def candidates(self):
        """The list of candidate responses.

        Raises:
            IncompleteIterationError: With `stream=True` if iteration over the stream was not completed.
        """
        if not self._done:
            raise IncompleteIterationError(_INCOMPLETE_ITERATION_MESSAGE)
        return self._result.candidates

    @property
    def parts(self):
        """A quick accessor equivalent to `self.candidates[0].content.parts`

        Raises:
            ValueError: If the candidate list does not contain exactly one candidate.
        """
        candidates = self.candidates
        if not candidates:
            raise ValueError(
                "The `response.parts` quick accessor only works for a single candidate, "
                "but none were returned. Check the `response.prompt_feedback` to see if the prompt was blocked."
            )
        if len(candidates) > 1:
            raise ValueError(
                "The `response.parts` quick accessor only works with a "
                "single candidate. With multiple candidates use "
                "result.candidates[index].text"
            )
        parts = candidates[0].content.parts
        return parts

    @property
    def text(self):
        """A quick accessor equivalent to `self.candidates[0].content.parts[0].text`

        Raises:
            ValueError: If the candidate list or parts list does not contain exactly one entry.
        """
        parts = self.parts
        if not parts:
            raise ValueError(
                "The `response.text` quick accessor only works when the response contains a valid "
                "`Part`, but none was returned. Check the `candidate.safety_ratings` to see if the "
                "response was blocked."
            )

        if len(parts) != 1 or "text" not in parts[0]:
            raise ValueError(
                "The `response.text` quick accessor only works for "
                "simple (single-`Part`) text responses. This response is not simple text. "
                "Use the `result.parts` accessor or the full "
                "`result.candidates[index].content.parts` lookup "
                "instead."
            )
        return parts[0].text

    @property
    def prompt_feedback(self):
        return self._result.prompt_feedback

    @property
    def usage_metadata(self):
        return self._result.usage_metadata

    def __str__(self) -> str:
        if self._done:
            _iterator = "None"
        else:
            _iterator = f"<{self._iterator.__class__.__name__}>"

        as_dict = type(self._result).to_dict(self._result)
        json_str = json.dumps(as_dict, indent=2)

        _result = f"glm.GenerateContentResponse({json_str})"
        _result = _result.replace("\n", "\n                    ")

        if self._error:
            _error = f",\nerror=<{self._error.__class__.__name__}> {self._error}"
        else:
            _error = ""

        return (
            textwrap.dedent(
                f"""\
                response:
                {type(self).__name__}(
                    done={self._done},
                    iterator={_iterator},
                    result={_result},
                )"""
            )
            + _error
        )

    __repr__ = __str__


@contextlib.contextmanager
def rewrite_stream_error():
    try:
        yield
    except (google.protobuf.json_format.ParseError, AttributeError) as e:
        raise google.api_core.exceptions.BadRequest(
            "Unknown error trying to retrieve streaming response. "
            "Please retry with `stream=False` for more details."
        )


GENERATE_CONTENT_RESPONSE_DOC = """Instances of this class manage the response of the `generate_content` method.

    These are returned by `GenerativeModel.generate_content` and `ChatSession.send_message`.
    This object is based on the low level `glm.GenerateContentResponse` class which just has `prompt_feedback`
    and `candidates` attributes. This class adds several quick accessors for common use cases.

    The same object type is returned for both `stream=True/False`.

    ### Streaming

    When you pass `stream=True` to `GenerativeModel.generate_content` or `ChatSession.send_message`,
    iterate over this object to receive chunks of the response:

    ```
    response = model.generate_content(..., stream=True):
    for chunk in response:
      print(chunk.text)
    ```

    `GenerateContentResponse.prompt_feedback` is available immediately but
    `GenerateContentResponse.candidates`, and all the attributes derived from them (`.text`, `.parts`),
    are only available after the iteration is complete.
    """

ASYNC_GENERATE_CONTENT_RESPONSE_DOC = (
    """This is the async version of `genai.GenerateContentResponse`."""
)


@string_utils.set_doc(GENERATE_CONTENT_RESPONSE_DOC)
class GenerateContentResponse(BaseGenerateContentResponse):
    @classmethod
    def from_iterator(cls, iterator: Iterable[glm.GenerateContentResponse]):
        iterator = iter(iterator)
        with rewrite_stream_error():
            response = next(iterator)

        return cls(
            done=False,
            iterator=iterator,
            result=response,
        )

    @classmethod
    def from_response(cls, response: glm.GenerateContentResponse):
        return cls(
            done=True,
            iterator=None,
            result=response,
        )

    def __iter__(self):
        # This is not thread safe.
        if self._done:
            for chunk in self._chunks:
                yield GenerateContentResponse.from_response(chunk)
            return

        # Always have the next chunk available.
        if len(self._chunks) == 0:
            self._chunks.append(next(self._iterator))

        for n in itertools.count():
            if self._error:
                raise self._error

            if n >= len(self._chunks) - 1:
                # Look ahead for a new item, so that you know the stream is done
                # when you yield the last item.
                if self._done:
                    return

                try:
                    item = next(self._iterator)
                except StopIteration:
                    self._done = True
                except Exception as e:
                    self._error = e
                    self._done = True
                else:
                    self._chunks.append(item)
                    self._result = _join_chunks([self._result, item])

            item = self._chunks[n]

            item = GenerateContentResponse.from_response(item)
            yield item

    def resolve(self):
        if self._done:
            return

        for _ in self:
            pass


@string_utils.set_doc(ASYNC_GENERATE_CONTENT_RESPONSE_DOC)
class AsyncGenerateContentResponse(BaseGenerateContentResponse):
    @classmethod
    async def from_aiterator(cls, iterator: AsyncIterable[glm.GenerateContentResponse]):
        iterator = aiter(iterator)  # type: ignore
        with rewrite_stream_error():
            response = await anext(iterator)  # type: ignore

        return cls(
            done=False,
            iterator=iterator,
            result=response,
        )

    @classmethod
    def from_response(cls, response: glm.GenerateContentResponse):
        return cls(
            done=True,
            iterator=None,
            result=response,
        )

    async def __aiter__(self):
        # This is not thread safe.
        if self._done:
            for chunk in self._chunks:
                yield GenerateContentResponse.from_response(chunk)
            return

        # Always have the next chunk available.
        if len(self._chunks) == 0:
            self._chunks.append(await anext(self._iterator))  # type: ignore

        for n in itertools.count():
            if self._error:
                raise self._error

            if n >= len(self._chunks) - 1:
                # Look ahead for a new item, so that you know the stream is done
                # when you yield the last item.
                if self._done:
                    return

                try:
                    item = await anext(self._iterator)  # type: ignore
                except StopAsyncIteration:
                    self._done = True
                except Exception as e:
                    self._error = e
                    self._done = True
                else:
                    self._chunks.append(item)
                    self._result = _join_chunks([self._result, item])

            item = self._chunks[n]

            item = GenerateContentResponse.from_response(item)
            yield item

    async def resolve(self):
        if self._done:
            return

        async for _ in self:
            pass
