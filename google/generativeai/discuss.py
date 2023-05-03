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

import dataclasses
import sys
import textwrap

from typing import Iterable, List, Optional, Union

import google.ai.generativelanguage as glm

from google.generativeai.client import get_default_discuss_client
from google.generativeai.client import get_default_discuss_async_client
from google.generativeai.types import discuss_types
from google.generativeai.types import model_types


def _make_message(content: discuss_types.MessageOptions) -> glm.Message:
    if isinstance(content, glm.Message):
        return content
    if isinstance(content, str):
        return glm.Message(content=content)
    else:
        return glm.Message(content)


def _make_messages(messages: discuss_types.MessagesOptions) -> List[glm.Message]:
    if isinstance(messages, (str, dict, glm.Message)):
        messages = [_make_message(messages)]
    else:
        messages = [_make_message(message) for message in messages]

    even_authors = set(msg.author for msg in messages[::2] if msg.author)
    if not even_authors:
        even_author = "0"
    elif len(even_authors) == 1:
        even_author = even_authors.pop()
    else:
        raise discuss_types.AuthorError("Authors are not strictly alternating")

    odd_authors = set(msg.author for msg in messages[1::2] if msg.author)
    if not odd_authors:
        odd_author = "1"
    elif len(odd_authors) == 1:
        odd_author = odd_authors.pop()
    else:
        raise discuss_types.AuthorError("Authors are not strictly alternating")

    if all(msg.author for msg in messages):
        return messages

    authors = [even_author, odd_author]
    for i, msg in enumerate(messages):
        msg.author = authors[i % 2]

    return messages


def _make_example(item: discuss_types.ExampleOptions) -> glm.Example:
    if isinstance(item, glm.Example):
        return item

    if isinstance(item, dict):
        item = item.copy()
        item["input"] = _make_message(item["input"])
        item["output"] = _make_message(item["output"])
        return glm.Example(item)

    if isinstance(item, Iterable):
        input, output = list(item)
        return glm.Example(input=_make_message(input), output=_make_message(output))

    # try anyway
    return glm.Example(item)


def _make_examples_from_flat(
    examples: List[discuss_types.MessageOptions],
) -> List[glm.Example]:
    if len(examples) % 2 != 0:
        raise ValueError(
            textwrap.dedent(
                """\
            You must pass `Primer` objects, pairs of messages, or an *even* number of messages, got: 
              {len(primers)} messages"""
            )
        )
    result = []
    pair = []
    for n, item in enumerate(examples):
        msg = _make_message(item)
        pair.append(msg)
        if n % 2 == 0:
            continue
        primer = glm.Example(
            input=pair[0],
            output=pair[1],
        )
        result.append(primer)
        pair = []
    return result


def _make_examples(examples: discuss_types.ExamplesOptions) -> List[glm.Example]:
    if isinstance(examples, glm.Example):
        return [examples]

    if isinstance(examples, dict):
        return [_make_example(examples)]

    examples = list(examples)

    if not examples:
        return examples

    first = examples[0]

    if isinstance(first, dict):
        if "content" in first:
            # These are `Messages`
            return _make_examples_from_flat(examples)
        else:
            if not ("input" in first and "output" in first):
                raise TypeError(
                    "To create an `Example` from a dict you must supply both `input` and an `output` keys"
                )
    else:
        if isinstance(first, discuss_types.MESSAGE_OPTIONS):
            return _make_examples_from_flat(examples)

    result = []
    for item in examples:
        result.append(_make_example(item))
    return result


def _make_message_prompt_dict(
    prompt: discuss_types.MessagePromptOptions = None,
    *,
    context: Optional[str] = None,
    examples: Optional[discuss_types.ExamplesOptions] = None,
    messages: Optional[discuss_types.MessagesOptions] = None,
) -> glm.MessagePrompt:
    if prompt is None:
        prompt = dict(
            context=context,
            examples=examples,
            messages=messages,
        )
    else:
        flat_prompt = (
            (context is not None) or (examples is not None) or (messages is not None)
        )
        if flat_prompt:
            raise ValueError(
                "You can't set `prompt`, and its fields `(context, examples, messages)`"
                " at the same time"
            )
        if isinstance(prompt, glm.MessagePrompt):
            return prompt
        elif isinstance(prompt, dict):  # Always check dict before Iterable.
            pass
        else:
            prompt = {"messages": prompt}

    keys = set(prompt.keys())
    if not keys.issubset(discuss_types.MESSAGE_PROMPT_KEYS):
        raise KeyError(
            f"Found extra entries in the prompt dictionary: {keys - discuss_types.MESSAGE_PROMPT_KEYS}"
        )

    examples = prompt.get("examples", None)
    if examples is not None:
        prompt["examples"] = _make_examples(examples)
    messages = prompt.get("messages", None)
    if messages is not None:
        prompt["messages"] = _make_messages(messages)

    prompt = {k: v for k, v in prompt.items() if v is not None}
    return prompt


def _make_message_prompt(
    prompt: discuss_types.MessagePromptOptions = None,
    *,
    context: Optional[str] = None,
    examples: Optional[discuss_types.ExamplesOptions] = None,
    messages: Optional[discuss_types.MessagesOptions] = None,
) -> glm.MessagePrompt:
    prompt = _make_message_prompt_dict(
        prompt=prompt, context=context, examples=examples, messages=messages
    )
    return glm.MessagePrompt(prompt)


def _make_generate_message_request(
    *,
    model: Optional[model_types.ModelNameOptions],
    context: Optional[str] = None,
    examples: Optional[discuss_types.ExamplesOptions] = None,
    messages: Optional[discuss_types.MessagesOptions] = None,
    temperature: Optional[float] = None,
    candidate_count: Optional[int] = None,
    top_p: Optional[float] = None,
    top_k: Optional[float] = None,
    prompt: Optional[discuss_types.MessagePromptOptions] = None,
) -> glm.GenerateMessageRequest:
    model = model_types.make_model_name(model)

    prompt = _make_message_prompt(
        prompt=prompt, context=context, examples=examples, messages=messages
    )

    return glm.GenerateMessageRequest(
        model=model,
        prompt=prompt,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        candidate_count=candidate_count,
    )


def set_doc(doc):
    def inner(f):
        f.__doc__ = doc
        return f

    return inner


DEFAULT_DISCUSS_MODEL = "models/chat-bison-001"


def chat(
    *,
    model: Optional[model_types.ModelNameOptions] = "models/chat-bison-001",
    context: Optional[str] = None,
    examples: Optional[discuss_types.ExamplesOptions] = None,
    messages: Optional[discuss_types.MessagesOptions] = None,
    temperature: Optional[float] = None,
    candidate_count: Optional[int] = None,
    top_p: Optional[float] = None,
    top_k: Optional[float] = None,
    prompt: Optional[discuss_types.MessagePromptOptions] = None,
    client: Optional[glm.DiscussServiceClient] = None,
) -> discuss_types.ChatResponse:
    """Calls the API and returns a `types.ChatResponse` containing the response.

    Args:
        model: Which model to call, as a string or a `types.Model`.
        context: Text that should be provided to the model first, to ground the response.

            If not empty, this `context` will be given to the model first before the
            `examples` and `messages`.

            This field can be a description of your prompt to the model to help provide
            context and guide the responses.

            Examples:

            * "Translate the phrase from English to French."
            * "Given a statement, classify the sentiment as happy, sad or neutral."

            Anything included in this field will take precedence over history in `messages`
            if the total input size exceeds the model's `Model.input_token_limit`.
        examples: Examples of what the model should generate.

            This includes both the user input and the response that the model should
            emulate.

            These `examples` are treated identically to conversation messages except
            that they take precedence over the history in `messages`:
            If the total input size exceeds the model's `input_token_limit` the input
            will be truncated. Items will be dropped from `messages` before `examples`
        messages: A snapshot of the conversation history sorted chronologically.

            Turns alternate between two authors.

            If the total input size exceeds the model's `input_token_limit` the input
            will be truncated: The oldest items will be dropped from `messages`.
        temperature: Controls the randomness of the output. Must be positive.

            Typical values are in the range: `[0.0,1.0]`. Higher values produce a
            more random and varied response. A temperature of zero will be deterministic.
        candidate_count: The **maximum** number of generated response messages to return.

            This value must be between `[1, 8]`, inclusive. If unset, this
            will default to `1`.

            Note: Only unique candidates are returned. Higher temperatures are more
            likely to produce unique candidates. Setting `temperature=0.0` will always
            return 1 candidate regardless of the `candidate_count`.
        top_k: The API uses combined [nucleus](https://arxiv.org/abs/1904.09751) and
            top-k sampling.

            `top_k` sets the maximum number of tokens to sample from on each step.
        top_p: The API uses combined [nucleus](https://arxiv.org/abs/1904.09751) and
           top-k sampling.

           `top_p` configures the nucleus sampling. It sets the maximum cumulative
            probability of tokens to sample from.

            For example, if the sorted probabilities are
            `[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]` a `top_p` of `0.8` will sample
            as `[0.625, 0.25, 0.125, 0, 0, 0].

            Typical values are in the `[0.9, 1.0]` range.
        prompt: You may pass a `types.MessagePromptOptions` **instead** of a
            setting `context`/`examples`/`messages`, but not both.
        client: If you're not relying on the default client, you pass a
            `glm.DiscussServiceClient` instead.

    Returns:
        A `types.ChatResponse` containing the model's reply.
    """
    request = _make_generate_message_request(
        model=model,
        context=context,
        examples=examples,
        messages=messages,
        temperature=temperature,
        candidate_count=candidate_count,
        top_p=top_p,
        top_k=top_k,
        prompt=prompt,
    )

    return _generate_response(client=client, request=request)


@set_doc(chat.__doc__)
async def chat_async(
    *,
    model: Optional[model_types.ModelNameOptions] = None,
    context: Optional[str] = None,
    examples: Optional[discuss_types.ExamplesOptions] = None,
    messages: Optional[discuss_types.MessagesOptions] = None,
    temperature: Optional[float] = None,
    candidate_count: Optional[int] = None,
    top_p: Optional[float] = None,
    top_k: Optional[float] = None,
    prompt: Optional[discuss_types.MessagePromptOptions] = None,
    client: Optional[glm.DiscussServiceAsyncClient] = None,
) -> discuss_types.ChatResponse:
    request = _make_generate_message_request(
        model=model,
        context=context,
        examples=examples,
        messages=messages,
        temperature=temperature,
        candidate_count=candidate_count,
        top_p=top_p,
        top_k=top_k,
        prompt=prompt,
    )

    return await _generate_response_async(client=client, request=request)


if (sys.version_info.major, sys.version_info.minor) >= (3, 10):
    DATACLASS_KWARGS = {"kw_only": True}
else:
    DATACLASS_KWARGS = {}


@set_doc(discuss_types.ChatResponse.__doc__)
@dataclasses.dataclass(**DATACLASS_KWARGS, init=False)
class ChatResponse(discuss_types.ChatResponse):
    _client: Optional[glm.DiscussServiceClient] = dataclasses.field(
        default=lambda: None, repr=False
    )

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    @set_doc(discuss_types.ChatResponse.last.__doc__)
    def last(self) -> str:
        return self.messages[-1]["content"]

    @last.setter
    def last(self, message: discuss_types.MessageOptions):
        message = _make_message(message)
        self.messages[-1] = message

    @set_doc(discuss_types.ChatResponse.reply.__doc__)
    def reply(
        self, message: discuss_types.MessageOptions
    ) -> discuss_types.ChatResponse:
        if isinstance(self._client, glm.DiscussServiceAsyncClient):
            raise TypeError(
                f"reply can't be called on an async client, use reply_async instead."
            )
        request = self.to_dict()
        request.pop("candidates")
        request["messages"] = list(request["messages"])
        request["messages"].append(_make_message(message))
        request = _make_generate_message_request(**request)
        return _generate_response(request=request, client=self._client)

    @set_doc(discuss_types.ChatResponse.reply.__doc__)
    async def reply_async(
        self, message: discuss_types.MessageOptions
    ) -> discuss_types.ChatResponse:
        if isinstance(self._client, glm.DiscussServiceClient):
            raise TypeError(
                f"reply_async can't be called on a non-async client, use reply instead."
            )
        request = self.to_dict()
        request.pop("candidates")
        request["messages"] = list(request["messages"])
        request["messages"].append(_make_message(message))
        request = _make_generate_message_request(**request)
        return await _generate_response_async(request=request, client=self._client)


def _build_chat_response(
    request: glm.GenerateMessageRequest,
    response: glm.GenerateMessageResponse,
    client: Union[glm.DiscussServiceClient, glm.DiscussServiceAsyncClient],
) -> ChatResponse:
    request = type(request).to_dict(request)
    prompt = request.pop("prompt")
    request["examples"] = prompt["examples"]
    request["context"] = prompt["context"]
    request["messages"] = prompt["messages"]

    response = type(response).to_dict(response)
    request["messages"].append(response["candidates"][0])
    request.setdefault("temperature", None)
    request.setdefault("candidate_count", None)

    return ChatResponse(
        _client=client, candidates=response["candidates"], **request
    )  # pytype: disable=missing-parameter


def _generate_response(
    request: glm.GenerateMessageRequest,
    client: Optional[glm.DiscussServiceClient] = None,
) -> ChatResponse:
    if client is None:
        client = get_default_discuss_client()

    response = client.generate_message(request)

    return _build_chat_response(request, response, client)


async def _generate_response_async(
    request: glm.GenerateMessageRequest,
    client: Optional[glm.DiscussServiceAsyncClient] = None,
) -> ChatResponse:
    if client is None:
        client = get_default_discuss_async_client()

    response = await client.generate_message(request)

    return _build_chat_response(request, response, client)


def count_message_tokens(
    *,
    prompt: discuss_types.MessagePromptOptions = None,
    context: Optional[str] = None,
    examples: Optional[discuss_types.ExamplesOptions] = None,
    messages: Optional[discuss_types.MessagesOptions] = None,
    model: str = DEFAULT_DISCUSS_MODEL,
    client: Optional[glm.DiscussServiceAsyncClient] = None,
):
    prompt = _make_message_prompt(
        prompt, context=context, examples=examples, messages=messages
    )

    if client is None:
        client = get_default_discuss_client()

    result = client.count_message_tokens(model=model, prompt=prompt)

    return type(result).to_dict(result)
