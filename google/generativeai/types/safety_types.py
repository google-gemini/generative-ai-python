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
from typing import Iterable, List, TypedDict

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


def convert_filters_to_enums(filters: Iterable[dict]) -> List[ContentFilterDict]:
    result = []
    for f in filters:
        f = f.copy()
        f["reason"] = BlockedReason(f["reason"])
        result.append(f)
    return result


class SafetyRatingDict(TypedDict):
    category: HarmCategory
    probability: HarmProbability

    __doc__ = docstring_utils.strip_oneof(glm.SafetyRating.__doc__)


def convert_rating_to_enum(rating: dict) -> SafetyRatingDict:
    return {
        "category": HarmCategory(rating["category"]),
        "probability": HarmProbability(rating["probability"]),
    }


def convert_ratings_to_enum(ratings: Iterable[dict]) -> List[SafetyRatingDict]:
    result = []
    for r in ratings:
        result.append(convert_rating_to_enum(r))
    return result


class SafetySettingDict(TypedDict):
    category: HarmCategory
    threshold: HarmBlockThreshold

    __doc__ = docstring_utils.strip_oneof(glm.SafetySetting.__doc__)


def convert_setting_to_enum(setting: dict) -> SafetySettingDict:
    return {
        "category": HarmCategory(setting["category"]),
        "threshold": HarmBlockThreshold(setting["threshold"]),
    }


class SafetyFeedbackDict(TypedDict):
    rating: SafetyRatingDict
    setting: SafetySettingDict

    __doc__ = docstring_utils.strip_oneof(glm.SafetyFeedback.__doc__)


def convert_safety_feedback_to_enums(
    safety_feedback: Iterable[dict],
) -> List[SafetyFeedbackDict]:
    result = []
    for sf in safety_feedback:
        result.append(
            {
                "rating": convert_rating_to_enum(sf["rating"]),
                "setting": convert_setting_to_enum(sf["setting"]),
            }
        )
    return result


def convert_candidate_enums(candidates):
    result = []
    for candidate in candidates:
        candidate = candidate.copy()
        candidate["safety_ratings"] = convert_ratings_to_enum(
            candidate["safety_ratings"]
        )
        result.append(candidate)
    return result
