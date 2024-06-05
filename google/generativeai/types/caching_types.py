# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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

import datetime
from typing import Optional, Union
from typing_extensions import TypedDict
import re

__all__ = ["ExpirationTypes", "ExpireTime", "TTL"]


_VALID_CACHED_CONTENT_NAME = r"([a-z0-9-\.]+)$"
NAME_ERROR_MESSAGE = (
    "The `name` must consist of alphanumeric characters (or `-` or `.`). Received: `{name}`"
)


def valid_cached_content_name(name: str) -> bool:
    return re.match(_VALID_CACHED_CONTENT_NAME, name) is not None


class TTL(TypedDict):
    # Represents datetime.datetime.now() + desired ttl
    seconds: int
    nanos: int = 0

class ExpireTime(TypedDict):
    # Represents seconds of UTC time since Unix epoch
    seconds: int
    nanos: int = 0


ExpirationTypes = Union[TTL, ExpireTime, int, datetime.timedelta, datetime.datetime]


def to_expiration(expiration: Optional[ExpirationTypes]) -> TTL:
    if isinstance(expiration, datetime.timedelta):  # consider `ttl`
        return {
            "seconds": int(expiration.total_seconds()),
            "nanos": int(expiration.microseconds * 1000),
        }
    elif isinstance(expiration, datetime.datetime):  # consider `expire_time`
        timestamp = expiration.timestamp()
        seconds = int(timestamp)
        nanos = int((seconds % 1) * 1000)
        return {
            "seconds": seconds,
            "nanos": nanos,
        }
    elif isinstance(expiration, dict):
        return expiration
    elif isinstance(expiration, int):  # consider `ttl`
        return {"seconds": expiration}
    else:
        raise TypeError(
            f"Could not convert input to `expire_time` \n'" f"  type: {type(expiration)}\n",
            expiration,
        )
