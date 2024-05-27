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

import dataclasses
import datetime
from typing import Any, Iterable, Optional

from google.generativeai.types.model_types import idecode_time
from google.generativeai.types import caching_types
from google.generativeai.types import content_types
from google.generativeai.utils import flatten_update_paths
from google.generativeai.client import get_default_cache_client

from google.protobuf import field_mask_pb2
import google.ai.generativelanguage as glm


@dataclasses.dataclass
class CachedContent:
    """Cached content resource."""

    name: str
    model: str
    create_time: datetime.datetime
    update_time: datetime.datetime
    expire_time: datetime.datetime

    # NOTE: Automatic CachedContent deletion using contextmanager is not P0(P1+).
    # Adding basic support for now.
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.delete()

    def _to_dict(self) -> glm.CachedContent:
        proto_paths = {
            "name": self.name,
            "model": self.model,
        }
        return glm.CachedContent(**proto_paths)

    def _apply_update(self, path, value):
        parts = path.split(".")
        for part in parts[:-1]:
            self = getattr(self, part)
        if parts[-1] == "ttl":
            value = self.expire_time + datetime.timedelta(seconds=value["seconds"])
            parts[-1] = "expire_time"
        setattr(self, parts[-1], value)

    @classmethod
    def _decode_cached_content(cls, cached_content: glm.CachedContent) -> CachedContent:
        # not supposed to get INPUT_ONLY repeated fields, but local gapic lib build
        # is returning these, hence setting including_default_value_fields to False
        cached_content = type(cached_content).to_dict(
            cached_content, including_default_value_fields=False
        )

        idecode_time(cached_content, "create_time")
        idecode_time(cached_content, "update_time")
        # always decode `expire_time` as Timestamp is returned
        # regardless of what was sent on input
        idecode_time(cached_content, "expire_time")
        return cls(**cached_content)

    @staticmethod
    def _prepare_create_request(
        model: str,
        name: str | None = None,
        system_instruction: Optional[content_types.ContentType] = None,
        contents: Optional[content_types.ContentsType] = None,
        tools: Optional[content_types.FunctionLibraryType] = None,
        tool_config: Optional[content_types.ToolConfigType] = None,
        ttl: Optional[caching_types.ExpirationTypes] = datetime.timedelta(hours=1),
    ) -> glm.CreateCachedContentRequest:
        """Prepares a CreateCachedContentRequest."""
        if name is not None:
            if not caching_types.valid_cached_content_name(name):
                raise ValueError(caching_types.NAME_ERROR_MESSAGE.format(name=name))

            name = "cachedContents/" + name

        if "/" not in model:
            model = "models/" + model

        if system_instruction:
            system_instruction = content_types.to_content(system_instruction)

        tools_lib = content_types.to_function_library(tools)
        if tools_lib:
            tools_lib = tools_lib.to_proto()

        if tool_config:
            tool_config = content_types.to_tool_config(tool_config)

        if contents:
            contents = content_types.to_contents(contents)

        if ttl:
            ttl = caching_types.to_ttl(ttl)

        cached_content = glm.CachedContent(
            name=name,
            model=model,
            system_instruction=system_instruction,
            contents=contents,
            tools=tools_lib,
            tool_config=tool_config,
            ttl=ttl,
        )

        return glm.CreateCachedContentRequest(cached_content=cached_content)

    @classmethod
    def create(
        cls,
        model: str,
        name: str | None = None,
        system_instruction: Optional[content_types.ContentType] = None,
        contents: Optional[content_types.ContentsType] = None,
        tools: Optional[content_types.FunctionLibraryType] = None,
        tool_config: Optional[content_types.ToolConfigType] = None,
        ttl: Optional[caching_types.ExpirationTypes] = datetime.timedelta(hours=1),
        client: glm.CacheServiceClient | None = None,
    ) -> CachedContent:
        """Creates CachedContent resource.

        Args:
            model: The name of the `Model` to use for cached content
                    Format: models/{model}. Cached content resource can be only
                    used with model it was created for.
            name: The resource name referring to the cached content.
            system_instruction: Developer set system instruction.
            contents: Contents to cache.
            tools: A list of `Tools` the model may use to generate response.
            tool_config: Config to apply to all tools.
            ttl: TTL for cached resource (in seconds). Defaults to 1 hour.

        Returns:
            `CachedContent` resource with specified name.
        """
        if client is None:
            client = get_default_cache_client()

        request = cls._prepare_create_request(
            model=model,
            name=name,
            system_instruction=system_instruction,
            contents=contents,
            tools=tools,
            tool_config=tool_config,
            ttl=ttl,
        )

        response = client.create_cached_content(request)
        return cls._decode_cached_content(response)

    @classmethod
    def get(cls, name: str, client: glm.CacheServiceClient | None = None) -> CachedContent:
        """Fetches required `CachedContent` resource.

        Args:
            name: name: The resource name referring to the cached content.

        Returns:
            `CachedContent` resource with specified name.
        """
        if client is None:
            client = get_default_cache_client()

        if "cachedContents/" not in name:
            name = "cachedContents/" + name

        request = glm.GetCachedContentRequest(name=name)
        response = client.get_cached_content(request)
        return cls._decode_cached_content(response)

    @classmethod
    def list(
        cls, page_size: Optional[int] = 1, client: glm.CacheServiceClient | None = None
    ) -> Iterable[CachedContent]:
        """Lists `CachedContent` objects associated with the project.

        Args:
            page_size: The maximum number of permissions to return (per page).
            The service may return fewer `CachedContent` objects.

        Returns:
            A paginated list of `CachedContent` objects.
        """
        if client is None:
            client = get_default_cache_client()

        request = glm.ListCachedContentsRequest(page_size=page_size)
        for cached_content in client.list_cached_contents(request):
            yield cls._decode_cached_content(cached_content)

    def delete(self, client: glm.CachedServiceClient | None = None) -> None:
        """Deletes `CachedContent` resource.

        Args:
            name: The resource name referring to the cached content.
                Format: cachedContents/{id}.
        """
        if client is None:
            client = get_default_cache_client()

        request = glm.DeleteCachedContentRequest(name=self.name)
        client.delete_cached_content(request)
        return

    def update(
        self,
        updates: dict[str, Any],
        client: glm.CacheServiceClient | None = None,
    ) -> CachedContent:
        """Updates requested `CachedContent` resource.

        Args:
            updates: The list of fields to update.
                     Currently only `ttl/expire_time` is supported as an update path.

        Returns:
            `CachedContent` object with specified updates.
        """
        if client is None:
            client = get_default_cache_client()

        updates = flatten_update_paths(updates)
        for update_path in updates:
            if update_path == "ttl":
                updates = updates.copy()
                update_path_val = updates.get(update_path)
                updates[update_path] = caching_types.to_ttl(update_path_val)
            else:
                raise ValueError(
                    f"As of now, only `ttl` can be updated for `CachedContent`. Got: `{update_path}` instead."
                )
        field_mask = field_mask_pb2.FieldMask()

        for path in updates.keys():
            field_mask.paths.append(path)
        for path, value in updates.items():
            self._apply_update(path, value)

        request = glm.UpdateCachedContentRequest(
            cached_content=self._to_dict(), update_mask=field_mask
        )
        client.update_cached_content(request)
        return self
