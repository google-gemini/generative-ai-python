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

import abc
import dataclasses
from typing import Iterator, List, Optional, Union

__all__ = [
    "Model",
    "ModelNameOptions",
    "ModelsIterable",
]


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
    supported_generation_methods: List[str]
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    top_k: Optional[int] = None


ModelNameOptions = Union[str, Model]


def make_model_name(name: ModelNameOptions):
    if isinstance(name, Model):
        name = name.name
    return name


class ModelsIterable(abc.ABC):
    """Iterate over this to yield `types.Model` objects."""

    @abc.abstractmethod
    def __iter__(self) -> Iterator[Model]:
        pass


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
