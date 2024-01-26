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

import abc
import dataclasses
from typing import Any, Dict, List, TypedDict, Optional, Union

import google.ai.generativelanguage as glm

from google.generativeai import string_utils
from google.generativeai.types import safety_types
from google.generativeai.types import citation_types
from google.generativeai.types import content_types

__all__ = ["Answer"]

""" BlockReason = glm.InputFeedback.BlockReason

BlockReasonOptions = Union[int, str, BlockReason]

_BLOCK_REASONS: dict[BlockReasonOptions, BlockReason] = {
    BlockReason.BLOCK_REASON_UNSPECIFIED: BlockReason.BLOCK_REASON_UNSPECIFIED,
    0: BlockReason.BLOCK_REASON_UNSPECIFIED,
    "block_reason_unspecified": BlockReason.BLOCK_REASON_UNSPECIFIED,
    "unspecified": BlockReason.BLOCK_REASON_UNSPECIFIED,
    BlockReason.SAFETY: BlockReason.SAFETY,
    1: BlockReason.SAFETY,
    "block_reason_safety": BlockReason.SAFETY,
    "safety": BlockReason.SAFETY,
    BlockReason.OTHER: BlockReason.OTHER,
    2: BlockReason.OTHER,
    "block_reason_other": BlockReason.OTHER,
    "other": BlockReason.OTHER,
} """

FinishReason = glm.Candidate.FinishReason

FinishReasonOptions = Union[int, str, FinishReason]

_FINISH_REASONS: dict[FinishReasonOptions, FinishReason] = {
    FinishReason.FINISH_REASON_UNSPECIFIED: FinishReason.FINISH_REASON_UNSPECIFIED,
    0: FinishReason.FINISH_REASON_UNSPECIFIED,
    "finish_reason_unspecified": FinishReason.FINISH_REASON_UNSPECIFIED,
    "unspecified": FinishReason.FINISH_REASON_UNSPECIFIED,
    FinishReason.STOP: FinishReason.STOP,
    1: FinishReason.STOP,
    "finish_reason_stop": FinishReason.STOP,
    "stop": FinishReason.STOP,
    FinishReason.MAX_TOKENS: FinishReason.MAX_TOKENS,
    2: FinishReason.MAX_TOKENS,
    "finish_reason_max_tokens": FinishReason.MAX_TOKENS,
    "max_tokens": FinishReason.MAX_TOKENS,
    FinishReason.SAFETY: FinishReason.SAFETY,
    3: FinishReason.SAFETY,
    "finish_reason_safety": FinishReason.SAFETY,
    "safety": FinishReason.SAFETY,
    FinishReason.RECITATION: FinishReason.RECITATION,
    4: FinishReason.RECITATION,
    "finish_reason_recitation": FinishReason.RECITATION,
    "recitation": FinishReason.RECITATION,
    FinishReason.OTHER: FinishReason.OTHER,
    5: FinishReason.OTHER,
    "finish_reason_other": FinishReason.OTHER,
    "other": FinishReason.OTHER,
}


def to_finish_reason(x: FinishReasonOptions) -> FinishReason:
    if isinstance(x, str):
        x = x.lower()
    return _FINISH_REASONS[x]


class AttributionSourceId(TypedDict):
    passage_id: str
    part_index: int


class GroundingAttribution(TypedDict):
    source_id: AttributionSourceId
    content: content_types.ContentType


class Candidate(TypedDict):
    index: Optional[int]
    content: content_types.ContentType
    finish_reason: Optional[glm.Candidate.FinishReason]
    finish_message: Optional[str]
    safety_ratings: List[safety_types.SafetyRatingDict | None]
    citation_metadata: citation_types.CitationMetadataDict | None
    token_count: int
    grounding_attribution: list[GroundingAttribution]
