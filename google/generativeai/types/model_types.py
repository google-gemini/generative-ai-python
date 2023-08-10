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
"""Type definitions for the models service."""
from __future__ import annotations

import re
import abc
import dataclasses
import datetime
from typing import Iterable, TypedDict, Union

import google.ai.generativelanguage as glm

__all__ = [
    "Model",
    "AnyModelNameOptions",
    "BaseModelNameOptions",
    "TunedModelNameOptions",
    "ModelsIterable",
    "TunedModel",
    "TunedModelState",
]

TunedModelState = glm.TunedModel.State


@dataclasses.dataclass
class Model:
    """A dataclass representation of a `glm.Model`.

    Attributes:
        name: The resource name of the `Model`. Format: `models/{model}` with a `{model}` naming convention of:
          "{base_model_id}-{version}". For example: `models/chat-bison-001`.
        base_model_id: The base name of the model. For example: `chat-bison`.
        version:  The major version number of the model. For example: `001`.
        display_name: The human-readable name of the model. E.g. `"Chat Bison"`. The name can be up to 128 characters
           long and can consist of any UTF-8 characters.
        description: A short description of the model.
        input_token_limit: Maximum number of input tokens allowed for this model.
        output_token_limit: Maximum number of output tokens available for this model.
        supported_generation_methods: lists which methods are supported by the model. The method names are defined as
           Pascal case strings, such as `generateMessage` which correspond to API methods.
    """

    name: str
    base_model_id: str
    version: str
    display_name: str
    description: str
    input_token_limit: int
    output_token_limit: int
    supported_generation_methods: list[str]
    temperature: float | None = None
    top_p: float | None = None
    top_k: int | None = None


@dataclasses.dataclass
class TunedModel:
    """A dataclass representation of a `glm.TunedModel`."""

    name: str | None = None
    source_model: str | Model | TunedModel | None = None
    base_model: str | None = None
    display_name: str | None = None
    description: str | None = None
    temperature: float | None = None
    top_p: float | None = None
    top_k: float | None = None
    state: glm.TunedModel.State | None = None
    create_time: datetime.datetime | None = None
    update_time: datetime.datetime | None = None
    tuning_task: TuningTask | None = None


@dataclasses.dataclass
class TuningTask:
    start_time: datetime.datetime | None
    complete_time: datetime.datetime | None
    snapshots: list[TuningSnapshot] | None
    training_data: list[TuningExampleDict]
    hyperparameters: Hyperparameters


class TuningExampleDict(TypedDict):
    model_input: str
    output: str


TuningExampleOptions = Union[TuningExampleDict, glm.TuningExample, tuple[str, str]]
TuningDataOptions = (
    glm.Dataset | Iterable[TuningExampleOptions]
)  # TODO(markdaoust): csv, json, pandas, np


@dataclasses.dataclass
class TuningSnapshot:
    step: int
    epoch: int
    mean_score: float
    compute_time: datetime.datetime


@dataclasses.dataclass
class Hyperparameters:
    epoch_count: int
    batch_size: int
    learning_rate: float


BaseModelNameOptions = Union[str, Model, glm.Model]
TunedModelNameOptions = Union[str, TunedModel, glm.TunedModel]
AnyModelNameOptions = Union[str, Model, glm.Model, TunedModel, glm.TunedModel]


def make_model_name(name: AnyModelNameOptions):
    if isinstance(name, (Model, glm.Model, TunedModel, glm.TunedModel)):
        name = name.name
    elif isinstance(name, str):
        name = name
    else:
        raise TypeError("Expected: str, Model, or TunedModel")

    if not (name.startswith("models/") or name.startswith("tunedModels/")):
        raise ValueError("Model names should start with `models/` or `tunedModels/`")

    return name


ModelsIterable = Iterable[Model]
TunedModelsIterable = Iterable[TunedModel]


@dataclasses.dataclass
class TokenCount:
    """A dataclass representation of a `glm.TokenCountResponse`.

    Attributes:
        token_count: The number of tokens returned by the model's tokenizer for the `input_text`.
        token_count_limit:
    """

    token_count: int
    token_count_limit: int

    def over_limit(self):
        return self.token_count > self.token_count_limit
