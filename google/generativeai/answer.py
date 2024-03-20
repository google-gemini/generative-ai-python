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
from collections.abc import Iterable
import itertools
from typing import Any, Iterable, Union, Mapping, Optional, TypedDict

import google.ai.generativelanguage as glm

from google.generativeai.client import (
    get_default_generative_client,
    get_default_generative_async_client,
)
from google.generativeai import string_utils
from google.generativeai.types import model_types
from google.generativeai import models
from google.generativeai.types import safety_types
from google.generativeai.types import content_types
from google.generativeai.types import answer_types
from google.generativeai.types import retriever_types
from google.generativeai.types.retriever_types import MetadataFilter

DEFAULT_ANSWER_MODEL = "models/aqa"

AnswerStyle = glm.GenerateAnswerRequest.AnswerStyle

AnswerStyleOptions = Union[int, str, AnswerStyle]

_ANSWER_STYLES: dict[AnswerStyleOptions, AnswerStyle] = {
    AnswerStyle.ANSWER_STYLE_UNSPECIFIED: AnswerStyle.ANSWER_STYLE_UNSPECIFIED,
    0: AnswerStyle.ANSWER_STYLE_UNSPECIFIED,
    "answer_style_unspecified": AnswerStyle.ANSWER_STYLE_UNSPECIFIED,
    "unspecified": AnswerStyle.ANSWER_STYLE_UNSPECIFIED,
    AnswerStyle.ABSTRACTIVE: AnswerStyle.ABSTRACTIVE,
    1: AnswerStyle.ABSTRACTIVE,
    "answer_style_abstractive": AnswerStyle.ABSTRACTIVE,
    "abstractive": AnswerStyle.ABSTRACTIVE,
    AnswerStyle.EXTRACTIVE: AnswerStyle.EXTRACTIVE,
    2: AnswerStyle.EXTRACTIVE,
    "answer_style_extractive": AnswerStyle.EXTRACTIVE,
    "extractive": AnswerStyle.EXTRACTIVE,
    AnswerStyle.VERBOSE: AnswerStyle.VERBOSE,
    3: AnswerStyle.VERBOSE,
    "answer_style_verbose": AnswerStyle.VERBOSE,
    "verbose": AnswerStyle.VERBOSE,
}


def to_answer_style(x: AnswerStyleOptions) -> AnswerStyle:
    if isinstance(x, str):
        x = x.lower()
    return _ANSWER_STYLES[x]


GroundingPassageOptions = (
    Union[glm.GroundingPassage, tuple[str, content_types.ContentType], content_types.ContentType],
)

GroundingPassagesOptions = Union[
    glm.GroundingPassages,
    Iterable[GroundingPassageOptions],
    Mapping[str, content_types.ContentType],
]


def _make_grounding_passages(source: GroundingPassagesOptions) -> glm.GroundingPassages:
    """
    Converts the `source` into a `glm.GroundingPassage`. A `GroundingPassages` contains a list of
    `glm.GroundingPassage` objects, which each contain a `glm.Contant` and a string `id`.

    Args:
        source: `Content` or a `GroundingPassagesOptions` that will be converted to glm.GroundingPassages.

    Return:
        `glm.GroundingPassages` to be passed into `glm.GenerateAnswer`.
    """
    if isinstance(source, glm.GroundingPassages):
        return source

    if not isinstance(source, Iterable):
        raise TypeError(
            f"`source` must be a valid `GroundingPassagesOptions` type object got a: `{type(source)}`."
        )

    passages = []
    if isinstance(source, Mapping):
        source = source.items()

    for n, data in enumerate(source):
        if isinstance(data, glm.GroundingPassage):
            passages.append(data)
        elif isinstance(data, tuple):
            id, content = data  # tuple must have exactly 2 items.
            passages.append({"id": id, "content": content_types.to_content(content)})
        else:
            passages.append({"id": str(n), "content": content_types.to_content(data)})

    return glm.GroundingPassages(passages=passages)


SourceNameType = Union[
    str, retriever_types.Corpus, glm.Corpus, retriever_types.Document, glm.Document
]


class SemanticRetrieverConfigDict(TypedDict):
    source: SourceNameType
    query: content_types.ContentsType
    metadata_filter: Optional[Iterable[MetadataFilter]]
    max_chunks_count: Optional[int]
    minimum_relevance_score: Optional[float]


SemanticRetrieverConfigOptions = Union[
    SourceNameType,
    SemanticRetrieverConfigDict,
    glm.SemanticRetrieverConfig,
]


def _maybe_get_source_name(source) -> str | None:
    if isinstance(source, str):
        return source
    elif isinstance(
        source, (retriever_types.Corpus, glm.Corpus, retriever_types.Document, glm.Document)
    ):
        return source.name
    else:
        return None


def _make_semantic_retriever_config(
    source: SemanticRetrieverConfigOptions,
    query: content_types.ContentsType,
) -> glm.SemanticRetrieverConfig:
    if isinstance(source, glm.SemanticRetrieverConfig):
        return source

    name = _maybe_get_source_name(source)
    if name is not None:
        source = {"source": name}
    else:
        source["source"] = _maybe_get_source_name(source["source"])

    if source["query"] is None:
        source['query'] = query
    elif isinstance(source["query"], str):
        source["query"] = content_types.to_content(source["query"])

    return glm.SemanticRetrieverConfig(source)


def _make_generate_answer_request(
    *,
    model: model_types.AnyModelNameOptions = DEFAULT_ANSWER_MODEL,
    contents: content_types.ContentsType,
    inline_passages: GroundingPassagesOptions | None,
    semantic_retriever_config: SemanticRetrieverConfigOptions | None,
    answer_style: AnswerStyle | None = None,
    safety_settings: safety_types.SafetySettingOptions | None = None,
    temperature: float | None = None,
) -> glm.GenerateAnswerRequest:
    """
    Calls the API to generate a grounded answer from the model.

    Args:
        model: Name of the model used to generate the grounded response.
        contents: Content of the current conversation with the model. For single-turn query, this is a
            single question to answer. For multi-turn queries, this is a repeated field that contains
            conversation history and the last `Content` in the list containing the question.
        grounding_source: Sources in which to grounding the answer.
        answer_style: Style for grounded answers.
        safety_settings: Safety settings for generated output.
        temperature: The temperature for randomness in the output.

    Returns:
        Call for glm.GenerateAnswerRequest().
    """
    model = model_types.make_model_name(model)

    contents = content_types.to_contents(contents)

    if safety_settings:
        safety_settings = safety_types.normalize_safety_settings(
            safety_settings, harm_category_set="new"
        )

    if inline_passages is not None and semantic_retriever_config is not None:
        raise ValueError("Either inline_passages xor semantic_retriever_config must be set, not both.")
    if inline_passages is not None and semantic_retriever_config is None:
        inline_passages = _make_grounding_passages(inline_passages)
    elif semantic_retriever_config is not None and inline_passages is None:
        semantic_retriever_config = _make_semantic_retriever_config(
            semantic_retriever_config, contents[-1]
        )
    else:
        TypeError(
            f"The source must be either an `inline_passages` xor `semantic_retriever_config`, but both are `None`"
        )

    if answer_style:
        answer_style = to_answer_style(answer_style)

    return glm.GenerateAnswerRequest(
        model=model,
        contents=contents,
        inline_passages=inline_passages,
        semantic_retriever=semantic_retriever_config,
        safety_settings=safety_settings,
        temperature=temperature,
        answer_style=answer_style,
    )


def generate_answer(
    *,
    model: model_types.AnyModelNameOptions = DEFAULT_ANSWER_MODEL,
    contents: content_types.ContentsType,
    inline_passages: GroundingPassagesOptions | None,
    semantic_retriever: SemanticRetrieverConfigOptions | None,
    answer_style: AnswerStyle | None = None,
    safety_settings: safety_types.SafetySettingOptions | None = None,
    temperature: float | None = None,
    client: glm.GenerativeServiceClient | None = None,
):
    """
    Calls the API and returns a `types.Answer` containing the answer.

    Args:
        model: Which model to call, as a string or a `types.Model`.
        question: The question to be answered by the model, grounded in the
                provided source.
        grounding_source: Source indicating the passages in which the answer should be grounded.
        answer_style: Style in which the grounded answer should be returned.
        safety_settings: Safety settings for generated output. Defaults to None.
        client: If you're not relying on a default client, you pass a `glm.TextServiceClient` instead.

    Returns:
        A `types.Answer` containing the model's text answer response.
    """
    if client is None:
        client = get_default_generative_client()

    request = _make_generate_answer_request(
        model=model,
        contents=contents,
        inline_passages=inline_passages,
        semantic_retriever_config=semantic_retriever,
        safety_settings=safety_settings,
        temperature=temperature,
        answer_style=answer_style,
    )

    response = client.generate_answer(request)

    return response


async def generate_answer_async(
    *,
    model: model_types.AnyModelNameOptions = DEFAULT_ANSWER_MODEL,
    contents: content_types.ContentsType,
    inline_passages: GroundingPassagesOptions | None,
    semantic_retriever: SemanticRetrieverConfigOptions | None,
    answer_style: AnswerStyle | None = None,
    safety_settings: safety_types.SafetySettingOptions | None = None,
    temperature: float | None = None,
    client: glm.GenerativeServiceClient | None = None,
):
    """
    Calls the API and returns a `types.Answer` containing the answer.

    Args:
        model: Which model to call, as a string or a `types.Model`.
        question: The question to be answered by the model, grounded in the
                provided source.
        grounding_source: Source indicating the passages in which the answer should be grounded.
        answer_style: Style in which the grounded answer should be returned.
        safety_settings: Safety settings for generated output. Defaults to None.
        client: If you're not relying on a default client, you pass a `glm.TextServiceClient` instead.

    Returns:
        A `types.Answer` containing the model's text answer response.
    """
    if client is None:
        client = get_default_generative_async_client()

    request = _make_generate_answer_request(
        model=model,
        contents=contents,
        inline_passages=inline_passages,
        semantic_retriever_config=semantic_retriever,
        safety_settings=safety_settings,
        temperature=temperature,
        answer_style=answer_style,
    )

    response = await client.generate_answer(request)

    return response
