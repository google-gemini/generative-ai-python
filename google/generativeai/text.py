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

from typing import List, Iterable, Iterator, Optional, Union

import google.ai.generativelanguage as glm

from google.generativeai.client import get_default_text_client
from google.generativeai.types import text_types
from google.generativeai.types import model_types


def _make_text_prompt(prompt: Union[str, dict[str, str]]) -> glm.TextPrompt:
    if isinstance(prompt, str):
        return glm.TextPrompt(text=prompt)
    elif isinstance(prompt, dict):
        return glm.TextPrompt(prompt)
    else:
        TypeError("Expected string or dictionary for text prompt.")


def _make_generate_text_request(
    *,
    model: model_types.ModelNameOptions = "models/chat-lamda-001",
    prompt: Optional[str] = None,
    temperature: Optional[float] = None,
    candidate_count: Optional[int] = None,
    max_output_tokens: Optional[int] = None,
    top_p: Optional[int] = None,
    top_k: Optional[int] = None,
    stop_sequences: Union[str, Iterable[str]] = None,
) -> glm.GenerateTextRequest:
    model = model_types.make_model_name(model)
    prompt = _make_text_prompt(prompt=prompt)
    if isinstance(stop_sequences, str):
        stop_sequences = [stop_sequences]
    if stop_sequences:
        stop_sequences = list(stop_sequences)

    return glm.GenerateTextRequest(
        model=model,
        prompt=prompt,
        temperature=temperature,
        candidate_count=candidate_count,
        max_output_tokens=max_output_tokens,
        top_p=top_p,
        top_k=top_k,
        stop_sequences=stop_sequences,
    )


def generate_text(
    *,
    model: Optional[model_types.ModelNameOptions] = "models/text-bison-001",
    prompt: str,
    temperature: Optional[float] = None,
    candidate_count: Optional[int] = None,
    max_output_tokens: Optional[int] = None,
    top_p: Optional[float] = None,
    top_k: Optional[float] = None,
    stop_sequences: Union[str, Iterable[str]] = None,
    client: Optional[glm.TextServiceClient] = None,
) -> text_types.Completion:
    """Calls the API and returns a `types.Completion` containing the response.

    Args:
        model: Which model to call, as a string or a `types.Model`.
        prompt: Free-form input text given to the model. Given a prompt, the model will
                generate text that completes the input text.
        temperature: Controls the randomness of the output. Must be positive.
            Typical values are in the range: `[0.0,1.0]`. Higher values produce a
            more random and varied response. A temperature of zero will be deterministic.
        candidate_count: The **maximum** number of generated response messages to return.
            This value must be between `[1, 8]`, inclusive. If unset, this
            will default to `1`.

            Note: Only unique candidates are returned. Higher temperatures are more
            likely to produce unique candidates. Setting `temperature=0.0` will always
            return 1 candidate regardless of the `candidate_count`.
        max_output_tokens: Maximum number of tokens to include in a candidate. Must be greater
                           than zero. If unset, will default to 64.
        top_k: The API uses combined [nucleus](https://arxiv.org/abs/1904.09751) and top-k sampling.
            `top_k` sets the maximum number of tokens to sample from on each step.
        top_p: The API uses combined [nucleus](https://arxiv.org/abs/1904.09751) and top-k sampling.
            `top_p` configures the nucleus sampling. It sets the maximum cumulative
            probability of tokens to sample from.
            For example, if the sorted probabilities are
            `[0.5, 0.2, 0.1, 0.1, 0.05, 0.05]` a `top_p` of `0.8` will sample
            as `[0.625, 0.25, 0.125, 0, 0, 0].
        stop_sequences: A set of up to 5 character sequences that will stop output generation.
          If specified, the API will stop at the first appearance of a stop
          sequence. The stop sequence will not be included as part of the response.
        client: If you're not relying on a default client, you pass a `glm.TextServiceClient` instead.

    Returns:
        A `types.Completion` containing the model's text completion response.
    """
    request = _make_generate_text_request(
        model=model,
        prompt=prompt,
        temperature=temperature,
        candidate_count=candidate_count,
        max_output_tokens=max_output_tokens,
        top_p=top_p,
        top_k=top_k,
        stop_sequences=stop_sequences,
    )

    return _generate_response(client=client, request=request)


@dataclasses.dataclass(init=False)
class Completion(text_types.Completion):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.result = None
        if self.candidates:
            self.result = self.candidates[0]["output"]


def _generate_response(
    request: glm.GenerateTextRequest, client: glm.TextServiceClient = None
) -> Completion:
    if client is None:
        client = get_default_text_client()

    response = client.generate_text(request)
    response = type(response).to_dict(response)

    return Completion(_client=client, **response)


def generate_embeddings(model: str, text: str, client: glm.TextServiceClient = None):
    """Calls the API to create an embedding for the text passed in.

    Args:
        model: Which model to call, as a string or a `types.Model`.

        text: Free-form input text given to the model. Given a string, the model will
              generate an embedding based on the input text.

        client: If you're not relying on a default client, you pass a `glm.TextServiceClient` instead.

    Returns:
        Dictionary containing the embedding (list of float values) for the input text.
    """
    if model is None:
        model = "models/chat-lamda-001"
    else:
        model = model_types.make_model_name(model)

    if client is None:
        client = get_default_text_client()

    embedding_request = glm.EmbedTextRequest(model=model, text=text)
    embedding_response = client.embed_text(embedding_request)

    embedding_dict = type(embedding_response).to_dict(embedding_response)

    embedding_dict["embedding"] = embedding_dict["embedding"]["value"]
    return embedding_dict
