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

import enum
from google.ai import generativelanguage as glm
from google.generativeai import docstring_utils
from typing import TypedDict

__all__ = [
    "HarmCategory",
    "HarmProbability",
    "HarmBlockThreshold",
    "BlockedReason",
    "ContentFilter",
    "SafetyRatingDict",
    "SafetySetting",
    "SafetyFeedbackDict",
]

# These are basic python enums, it's okay to expose them
HarmCategory = glm.HarmCategory
HarmProbability = glm.SafetyRating.HarmProbability
HarmBlockThreshold = glm.SafetySetting.HarmBlockThreshold
BlockedReason = glm.ContentFilter.BlockedReason


class ContentFilter(TypedDict):
    reason: BlockedReason
    message: str

    __doc__ = docstring_utils.strip_oneof(glm.ContentFilter.__doc__)


class SafetyRatingDict(TypedDict):
    category: HarmCategory
    probability: HarmProbability

    __doc__ = docstring_utils.strip_oneof(glm.SafetyRating.__doc__)


class SafetySetting(TypedDict):
    category: HarmCategory
    threshold: HarmBlockThreshold

    __doc__ = docstring_utils.strip_oneof(glm.SafetySetting.__doc__)


class SafetyFeedbackDict(TypedDict):
    rating: SafetyRatingDict
    setting: SafetySetting

    __doc__ = docstring_utils.strip_oneof(glm.SafetyFeedback.__doc__)
