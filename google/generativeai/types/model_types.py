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

import dataclasses
import datetime
import re
from typing import Any, Iterable, TypedDict, Union

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

TunedModelStateOptions = Union[None, str, int, TunedModelState]

# fmt: off
_TUNED_MODEL_STATES: dict[TunedModelStateOptions, TunedModelState] = {
    TunedModelState.ACTIVE: TunedModelState.ACTIVE,
    int(TunedModelState.ACTIVE): TunedModelState.ACTIVE,
    "active": TunedModelState.ACTIVE,

    TunedModelState.CREATING: TunedModelState.CREATING,
    int(TunedModelState.CREATING): TunedModelState.CREATING,
    "creating": TunedModelState.CREATING,

    TunedModelState.FAILED: TunedModelState.FAILED,
    int(TunedModelState.FAILED): TunedModelState.FAILED,
    "failed": TunedModelState.FAILED,

    TunedModelState.STATE_UNSPECIFIED: TunedModelState.STATE_UNSPECIFIED,
    int(TunedModelState.STATE_UNSPECIFIED): TunedModelState.STATE_UNSPECIFIED,
    "state_unspecified": TunedModelState.STATE_UNSPECIFIED,
    "unspecified": TunedModelState.STATE_UNSPECIFIED,
    None: TunedModelState.STATE_UNSPECIFIED,
}
# fmt: on


def to_tuned_model_state(x: TunedModelStateOptions) -> TunedModelState:
    if isinstance(x, str):
        x = x.lower()
    return _TUNED_MODEL_STATES[x]


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


def _fix_microseconds(match):
    # microseconds needs exactly 6 digits
    fraction = float(match.group(0))
    return f".{int(round(fraction*1e6)):06d}"


def idecode_time(parent: dict["str", Any], name: str):
    time = parent.pop(name, None)
    if time is not None:
        if "." in time:
            time = re.sub(r"\.\d+", _fix_microseconds, time)
            dt = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%fZ")
        else:
            dt = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%SZ")

        dt = dt.replace(tzinfo=datetime.timezone.utc)
        parent[name] = dt


def decode_tuned_model(tuned_model: glm.TunedModel | dict["str", Any]) -> TunedModel:
    if isinstance(tuned_model, glm.TunedModel):
        tuned_model = type(tuned_model).to_dict(
            tuned_model
        )  # pytype: disable=attribute-error
    tuned_model["state"] = to_tuned_model_state(tuned_model.pop("state", None))

    base_model = tuned_model.pop("base_model", None)
    tuned_model_source = tuned_model.pop("tuned_model_source", None)
    if base_model is not None:
        tuned_model["base_model"] = base_model
        tuned_model["source_model"] = base_model
    elif tuned_model_source is not None:
        tuned_model["base_model"] = tuned_model_source["base_model"]
        tuned_model["source_model"] = tuned_model_source["tuned_model"]

    idecode_time(tuned_model, "create_time")
    idecode_time(tuned_model, "update_time")

    task = tuned_model.pop("tuning_task", None)
    if task is not None:
        hype = task.pop("hyperparameters", None)
        if hype is not None:
            hype = Hyperparameters(**hype)
            task["hyperparameters"] = hype

        idecode_time(task, "start_time")
        idecode_time(task, "complete_time")

        snapshots = task.pop("snapshots", None)
        if snapshots is not None:
            for snap in snapshots:
                idecode_time(snap, "compute_time")
            task["snapshots"] = snapshots
        task = TuningTask(**task)
        tuned_model["tuning_task"] = task
    return TunedModel(**tuned_model)


@dataclasses.dataclass
class TunedModel:
    """A dataclass representation of a `glm.TunedModel`."""

    name: str | None = None
    source_model: str | None = None
    base_model: str | None = None
    display_name: str = ""
    description: str = ""
    temperature: float | None = None
    top_p: float | None = None
    top_k: float | None = None
    state: TunedModelState = TunedModelState.STATE_UNSPECIFIED
    create_time: datetime.datetime | None = None
    update_time: datetime.datetime | None = None
    tuning_task: TuningTask | None = None


@dataclasses.dataclass
class TuningTask:
    start_time: datetime.datetime | None = None
    complete_time: datetime.datetime | None = None
    snapshots: list[TuningSnapshot] = dataclasses.field(default_factory=list)
    hyperparameters: Hyperparameters | None = None


class TuningExampleDict(TypedDict):
    text_input: str
    output: str


TuningExampleOptions = Union[TuningExampleDict, glm.TuningExample, tuple[str, str]]
TuningDataOptions = Union[
    glm.Dataset, Iterable[TuningExampleOptions]
]  # TODO(markdaoust): csv, json, pandas, np


def encode_tuning_data(data: TuningDataOptions) -> glm.Dataset:
    if isinstance(data, glm.Dataset):
        return data

    new_data = list()
    for example in data:
        example = encode_tuning_example(example)
        new_data.append(example)
    return glm.Dataset(examples=glm.TuningExamples(examples=new_data))


def encode_tuning_example(example: TuningExampleOptions):
    if isinstance(example, tuple):
        example = glm.TuningExample(text_input=example[0], output=example[1])
    else:  # dict or  glm.TuningExample
        example = glm.TuningExample(example)
    return example


@dataclasses.dataclass
class TuningSnapshot:
    step: int
    epoch: int
    mean_score: float
    compute_time: datetime.datetime


@dataclasses.dataclass
class Hyperparameters:
    epoch_count: int = 0
    batch_size: int = 0
    learning_rate: float = 0.0


BaseModelNameOptions = Union[str, Model, glm.Model]
TunedModelNameOptions = Union[str, TunedModel, glm.TunedModel]
AnyModelNameOptions = Union[str, Model, glm.Model, TunedModel, glm.TunedModel]


def make_model_name(name: AnyModelNameOptions):
    if isinstance(name, (Model, glm.Model, TunedModel, glm.TunedModel)):
        name = name.name  # pytype: disable=attribute-error
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
