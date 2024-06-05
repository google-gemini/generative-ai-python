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

__all__ = ["TTL"]


_VALID_CACHED_CONTENT_NAME = r"([a-z0-9-\.]+)$"
NAME_ERROR_MESSAGE = (
    "The `name` must consist of alphanumeric characters (or `-` or `.`). Received: `{name}`"
)


def valid_cached_content_name(name: str) -> bool:
    return re.match(_VALID_CACHED_CONTENT_NAME, name) is not None


class TTL(TypedDict):
    seconds: int


ExpirationTypes = Union[TTL, int, datetime.timedelta]


def to_ttl(expiration: Optional[ExpirationTypes]) -> TTL:
    if isinstance(expiration, datetime.timedelta):
        return {"seconds": int(expiration.total_seconds())}
    elif isinstance(expiration, dict):
        return expiration
    elif isinstance(expiration, int):
        return {"seconds": expiration}
    else:
        raise TypeError(
            f"Could not convert input to `expire_time` \n'" f"  type: {type(expiration)}\n",
            expiration,
        )
