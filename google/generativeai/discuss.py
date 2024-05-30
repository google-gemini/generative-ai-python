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

import dataclasses
import sys
import textwrap

from typing import Iterable, List

import google.ai.generativelanguage as glm

from google.generativeai.client import get_default_discuss_client
from google.generativeai.client import get_default_discuss_async_client
from google.generativeai import string_utils
from google.generativeai import protos
from google.generativeai.types import discuss_types
from google.generativeai.types import helper_types
from google.generativeai.types import model_types
from google.generativeai.types import palm_safety_types


def _make_message(content: discuss_types.MessageOptions) -> protos.Message:
    """Creates a `protos.Message` object from the provided content."""
    if isinstance(content, protos.Message):
        return content
    if isinstance(content, str):
        return protos.Message(content=content)
    else:
        return protos.Message(content)


def _make_messages(
    messages: discuss_types.MessagesOptions,
) -> List[protos.Message]:
    """
    Creates a list of `protos.Message` objects from the provided messages.

    This function takes a variety of message content inputs, such as strings, dictionaries,
    or `protos.Message` objects, and creates a list of `protos.Message` objects. It ensures that
    the authors of the messages alternate appropriately. If authors are not provided,
    default authors are assigned based on their position in the list.

    Args:
        messages: The messages to convert.

    Returns:
        A list of `protos.Message` objects with alternating authors.
    """
    if isinstance(messages, (str, dict, protos.Message)):
        messages = [_make_message(messages)]
    else:
        messages = [_make_message(message) for message in messages]

    even_authors = set(msg.author for msg in messages[::2] if msg.author)
    if not even_authors:
        even_author = "0"
    elif len(even_authors) == 1:
        even_author = even_authors.pop()
    else:
        raise discuss_types.AuthorError(
            "Invalid sequence: Authors in the discussion must alternate strictly."
        )

    odd_authors = set(msg.author for msg in messages[1::2] if msg.author)
    if not odd_authors:
        odd_author = "1"
    elif len(odd_authors) == 1:
        odd_author = odd_authors.pop()
    else:
        raise discuss_types.AuthorError(
            "Invalid sequence: Authors in the discussion must alternate strictly."
        )

    if all(msg.author for msg in messages):
        return messages

    authors = [even_author, odd_author]
    for i, msg in enumerate(messages):
        msg.author = authors[i % 2]

    return messages


def _make_example(item: discuss_types.ExampleOptions) -> protos.Example:
    """Creates a `protos.Example` object from the provided item."""
    if isinstance(item, protos.Example):
        return item

    if isinstance(item, dict):
        item = item.copy()
        item["input"] = _make_message(item["input"])
        item["output"] = _make_message(item["output"])
        return protos.Example(item)

    if isinstance(item, Iterable):
        input, output = list(item)
        return protos.Example(input=_make_message(input), output=_make_message(output))

    # try anyway
    return protos.Example(item)


def _make_examples_from_flat(
    examples: List[discuss_types.MessageOptions],
) -> List[protos.Example]:
    """
    Creates a list of `protos.Example` objects from a list of message options.

    This function takes a list of `discuss_types.MessageOptions` and pairs them into
    `protos.Example` objects. The input examples must be in pairs to create valid examples.

    Args:
        examples: The list of `discuss_types.MessageOptions`.

    Returns:
        A list of `protos.Example objects` created by pairing up the provided messages.

    Raises:
        ValueError: If the provided list of examples is not of even length.
    """
    if len(examples) % 2 != 0:
        raise ValueError(
            textwrap.dedent(
                f"""\
                Invalid input: You must pass either `Primer` objects, pairs of messages, or an even number of messages. 
                Currently, {len(examples)} messages were provided, which is an odd number."""
            )
        )
    result = []
    pair = []
    for n, item in enumerate(examples):
        msg = _make_message(item)
        pair.append(msg)
        if n % 2 == 0:
            continue
        primer = protos.Example(
            input=pair[0],
            output=pair[1],
        )
        result.append(primer)
        pair = []
    return result


def _make_examples(
    examples: discuss_types.ExamplesOptions,
) -> List[protos.Example]:
    """
    Creates a list of `protos.Example` objects from the provided examples.

    This function takes various types of example content inputs and creates a list
    of `protos.Example` objects. It handles the conversion of different input types and ensures
    the appropriate structure for creating valid examples.

    Args:
        examples: The examples to convert.

    Returns:
        A list of `protos.Example` objects created from the provided examples.
    """
    if isinstance(examples, protos.Example):
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
                    "Invalid dictionary format: To create an `Example` instance, the dictionary must contain both `input` and `output` keys."
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
    context: str | None = None,
    examples: discuss_types.ExamplesOptions | None = None,
    messages: discuss_types.MessagesOptions | None = None,
) -> protos.MessagePrompt:
    """
    Creates a `protos.MessagePrompt` object from the provided prompt components.

    This function constructs a `protos.MessagePrompt` object using the provided `context`, `examples`,
    or `messages`. It ensures the proper structure and handling of the input components.

    Either pass a `prompt` or it's component `context`, `examples`, `messages`.

    Args:
        prompt: The complete prompt components.
        context: The context for the prompt.
        examples: The examples for the prompt.
        messages: The messages for the prompt.

    Returns:
        A `protos.MessagePrompt` object created from the provided prompt components.
    """
    if prompt is None:
        prompt = dict(
            context=context,
            examples=examples,
            messages=messages,
        )
    else:
        flat_prompt = (context is not None) or (examples is not None) or (messages is not None)
        if flat_prompt:
            raise ValueError(
                "Invalid configuration: Either `prompt` or its fields `(context, examples, messages)` should be set, but not both simultaneously."
            )
        if isinstance(prompt, protos.MessagePrompt):
            return prompt
        elif isinstance(prompt, dict):  # Always check dict before Iterable.
            pass
        else:
            prompt = {"messages": prompt}

    keys = set(prompt.keys())
    if not keys.issubset(discuss_types.MESSAGE_PROMPT_KEYS):
        raise KeyError(
            f"Invalid prompt dictionary: Extra entries found that are not recognized: {keys - discuss_types.MESSAGE_PROMPT_KEYS}. Please check the keys."
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
    context: str | None = None,
    examples: discuss_types.ExamplesOptions | None = None,
    messages: discuss_types.MessagesOptions | None = None,
) -> protos.MessagePrompt:
    """Creates a `protos.MessagePrompt` object from the provided prompt components."""
    prompt = _make_message_prompt_dict(
        prompt=prompt, context=context, examples=examples, messages=messages
    )
    return protos.MessagePrompt(prompt)


def _make_generate_message_request(
    *,
    model: model_types.AnyModelNameOptions | None,
    context: str | None = None,
    examples: discuss_types.ExamplesOptions | None = None,
    messages: discuss_types.MessagesOptions | None = None,
    temperature: float | None = None,
    candidate_count: int | None = None,
    top_p: float | None = None,
    top_k: float | None = None,
    prompt: discuss_types.MessagePromptOptions | None = None,
) -> protos.GenerateMessageRequest:
    """Creates a `protos.GenerateMessageRequest` object for generating messages."""
    model = model_types.make_model_name(model)

    prompt = _make_message_prompt(
        prompt=prompt, context=context, examples=examples, messages=messages
    )

    return protos.GenerateMessageRequest(
        model=model,
        prompt=prompt,
        temperature=temperature,
        top_p=top_p,
        top_k=top_k,
        candidate_count=candidate_count,
    )


DEFAULT_DISCUSS_MODEL = "models/chat-bison-001"


def chat(
    *,
    model: model_types.AnyModelNameOptions | None = "models/chat-bison-001",
    context: str | None = None,
    examples: discuss_types.ExamplesOptions | None = None,
    messages: discuss_types.MessagesOptions | None = None,
    temperature: float | None = None,
    candidate_count: int | None = None,
    top_p: float | None = None,
    top_k: float | None = None,
    prompt: discuss_types.MessagePromptOptions | None = None,
    client: glm.DiscussServiceClient | None = None,
    request_options: helper_types.RequestOptionsType | None = None,
) -> discuss_types.ChatResponse:
    """Calls the API to initiate a chat with a model using provided parameters

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
            as `[0.625, 0.25, 0.125, 0, 0, 0]`.

            Typical values are in the `[0.9, 1.0]` range.
        prompt: You may pass a `types.MessagePromptOptions` **instead** of a
            setting `context`/`examples`/`messages`, but not both.
        client: If you're not relying on the default client, you pass a
            `glm.DiscussServiceClient` instead.
        request_options: Options for the request.

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

    return _generate_response(client=client, request=request, request_options=request_options)


@string_utils.set_doc(chat.__doc__)
async def chat_async(
    *,
    model: model_types.AnyModelNameOptions | None = "models/chat-bison-001",
    context: str | None = None,
    examples: discuss_types.ExamplesOptions | None = None,
    messages: discuss_types.MessagesOptions | None = None,
    temperature: float | None = None,
    candidate_count: int | None = None,
    top_p: float | None = None,
    top_k: float | None = None,
    prompt: discuss_types.MessagePromptOptions | None = None,
    client: glm.DiscussServiceAsyncClient | None = None,
    request_options: helper_types.RequestOptionsType | None = None,
) -> discuss_types.ChatResponse:
    """Calls the API asynchronously to initiate a chat with a model using provided parameters"""
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

    return await _generate_response_async(
        client=client, request=request, request_options=request_options
    )


if (sys.version_info.major, sys.version_info.minor) >= (3, 10):
    DATACLASS_KWARGS = {"kw_only": True}
else:
    DATACLASS_KWARGS = {}


@string_utils.prettyprint
@string_utils.set_doc(discuss_types.ChatResponse.__doc__)
@dataclasses.dataclass(**DATACLASS_KWARGS, init=False)
class ChatResponse(discuss_types.ChatResponse):
    _client: glm.DiscussServiceClient | None = dataclasses.field(default=lambda: None, repr=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    @string_utils.set_doc(discuss_types.ChatResponse.last.__doc__)
    def last(self) -> str | None:
        if self.messages[-1]:
            return self.messages[-1]["content"]
        else:
            return None

    @last.setter
    def last(self, message: discuss_types.MessageOptions):
        message = _make_message(message)
        message = type(message).to_dict(message)
        self.messages[-1] = message

    @string_utils.set_doc(discuss_types.ChatResponse.reply.__doc__)
    def reply(
        self,
        message: discuss_types.MessageOptions,
        request_options: helper_types.RequestOptionsType | None = None,
    ) -> discuss_types.ChatResponse:
        if isinstance(self._client, glm.DiscussServiceAsyncClient):
            raise TypeError(
                "Invalid operation: The 'reply' method cannot be called on an asynchronous client. Please use the 'reply_async' method instead."
            )
        if self.last is None:
            raise ValueError(
                f"Invalid operation: No candidates returned from the model's last response. "
                f"Please inspect the '.filters' attribute to understand why responses were filtered out. Current filters: {self.filters}"
            )

        request = self.to_dict()
        request.pop("candidates")
        request.pop("filters", None)
        request["messages"] = list(request["messages"])
        request["messages"].append(_make_message(message))
        request = _make_generate_message_request(**request)
        return _generate_response(
            request=request, client=self._client, request_options=request_options
        )

    @string_utils.set_doc(discuss_types.ChatResponse.reply.__doc__)
    async def reply_async(
        self, message: discuss_types.MessageOptions
    ) -> discuss_types.ChatResponse:
        if isinstance(self._client, glm.DiscussServiceClient):
            raise TypeError(
                "Invalid method call: `reply_async` is not supported on a non-async client. Please use the `reply` method instead."
            )
        request = self.to_dict()
        request.pop("candidates")
        request.pop("filters", None)
        request["messages"] = list(request["messages"])
        request["messages"].append(_make_message(message))
        request = _make_generate_message_request(**request)
        return await _generate_response_async(request=request, client=self._client)


def _build_chat_response(
    request: protos.GenerateMessageRequest,
    response: protos.GenerateMessageResponse,
    client: glm.DiscussServiceClient | protos.DiscussServiceAsyncClient,
) -> ChatResponse:
    request = type(request).to_dict(request)
    prompt = request.pop("prompt")
    request["examples"] = prompt["examples"]
    request["context"] = prompt["context"]
    request["messages"] = prompt["messages"]

    response = type(response).to_dict(response)
    response.pop("messages")

    response["filters"] = palm_safety_types.convert_filters_to_enums(response["filters"])

    if response["candidates"]:
        last = response["candidates"][0]
    else:
        last = None
    request["messages"].append(last)
    request.setdefault("temperature", None)
    request.setdefault("candidate_count", None)

    return ChatResponse(_client=client, **response, **request)  # pytype: disable=missing-parameter


def _generate_response(
    request: protos.GenerateMessageRequest,
    client: glm.DiscussServiceClient | None = None,
    request_options: helper_types.RequestOptionsType | None = None,
) -> ChatResponse:
    if request_options is None:
        request_options = {}

    if client is None:
        client = get_default_discuss_client()

    response = client.generate_message(request, **request_options)

    return _build_chat_response(request, response, client)


async def _generate_response_async(
    request: protos.GenerateMessageRequest,
    client: glm.DiscussServiceAsyncClient | None = None,
    request_options: helper_types.RequestOptionsType | None = None,
) -> ChatResponse:
    if request_options is None:
        request_options = {}

    if client is None:
        client = get_default_discuss_async_client()

    response = await client.generate_message(request, **request_options)

    return _build_chat_response(request, response, client)


def count_message_tokens(
    *,
    prompt: discuss_types.MessagePromptOptions = None,
    context: str | None = None,
    examples: discuss_types.ExamplesOptions | None = None,
    messages: discuss_types.MessagesOptions | None = None,
    model: model_types.AnyModelNameOptions = DEFAULT_DISCUSS_MODEL,
    client: glm.DiscussServiceAsyncClient | None = None,
    request_options: helper_types.RequestOptionsType | None = None,
) -> discuss_types.TokenCount:
    """Calls the API to calculate the number of tokens used in the prompt."""

    model = model_types.make_model_name(model)
    prompt = _make_message_prompt(prompt, context=context, examples=examples, messages=messages)

    if request_options is None:
        request_options = {}

    if client is None:
        client = get_default_discuss_client()

    result = client.count_message_tokens(model=model, prompt=prompt, **request_options)

    return type(result).to_dict(result)
