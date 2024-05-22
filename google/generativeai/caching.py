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

from typing import Optional, Iterable

import google.ai.generativelanguage as glm

from google.generativeai.types import caching_types
from google.generativeai.types import content_types
from google.generativeai.client import get_default_cache_client


# alias for `caching_types.CachedContent`.
CachedContent = caching_types.CachedContent


def get_cached_content(name: str, client: glm.CacheServiceClient | None = None) -> CachedContent:
    """Fetches required `CachedContent` resource.

    Args:
        name: name: The resource name referring to the cached content.

    Returns:
        `CachedContent` resource with specified name.
    """
    return CachedContent.get(name=name, client=client)


def delete_cached_content(name: str, client: glm.CacheServiceClient | None = None) -> None:
    """Deletes `CachedContent` resource.

    Args:
        name: The resource name referring to the cached content.
              Format: cachedContents/{id}.
    """
    if client is None:
        client = get_default_cache_client()

    if "cachedContents/" not in name:
        name = "cachedContents/" + name

    request = glm.DeleteCachedContentRequest(name=name)
    client.delete_cached_content(request)
    return


def list_cached_contents(
    page_size: Optional[int] = 1, client: glm.CacheServiceClient | None = None
) -> Iterable[CachedContent]:
    """Lists `CachedContent` objects associated with the project.

    Args:
        page_size: The maximum number of permissions to return (per page). The service may return fewer `CachedContent` objects.

    Returns:
        A paginated list of `CachedContent` objects.
    """
    if client is None:
        client = get_default_cache_client()

    request = glm.ListCachedContentsRequest(page_size=page_size)
    for cached_content in client.list_cached_contents(request):
        yield caching_types.decode_cached_content(cached_content)
