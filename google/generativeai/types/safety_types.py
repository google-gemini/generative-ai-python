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
    "ContentFilterDict",
    "SafetyRatingDict",
    "SafetySettingDict",
    "SafetyFeedbackDict",
]

# These are basic python enums, it's okay to expose them
HarmCategory = glm.HarmCategory
HarmProbability = glm.SafetyRating.HarmProbability
HarmBlockThreshold = glm.SafetySetting.HarmBlockThreshold
BlockedReason = glm.ContentFilter.BlockedReason


class ContentFilterDict(TypedDict):
    reason: BlockedReason
    message: str

    __doc__ = docstring_utils.strip_oneof(glm.ContentFilter.__doc__)


def convert_filters_to_enums(filters):
    for f in filters:
        f["reason"] = BlockedReason(f["reason"])


class SafetyRatingDict(TypedDict):
    category: HarmCategory
    probability: HarmProbability

    __doc__ = docstring_utils.strip_oneof(glm.SafetyRating.__doc__)


def convert_rating_to_enum(setting):
    setting["category"] = HarmCategory(setting["category"])
    setting["probability"] = HarmProbability(setting["probability"])


class SafetySettingDict(TypedDict):
    category: HarmCategory
    threshold: HarmBlockThreshold

    __doc__ = docstring_utils.strip_oneof(glm.SafetySetting.__doc__)


def convert_setting_to_enum(setting):
    setting["category"] = HarmCategory(setting["category"])
    setting["threshold"] = HarmBlockThreshold(setting["threshold"])


class SafetyFeedbackDict(TypedDict):
    rating: SafetyRatingDict
    setting: SafetySettingDict

    __doc__ = docstring_utils.strip_oneof(glm.SafetyFeedback.__doc__)


def convert_safety_feedback_to_enums(safety_feedback):
    for sf in safety_feedback:
        convert_rating_to_enum(sf["rating"])
        convert_setting_to_enum(sf["setting"])
