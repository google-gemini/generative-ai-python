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

import google.ai.generativelanguage as glm

from google.generativeai.types import permission_types


def _construct_and_validate_name(
        name: str | None = None,
        corpus_name: str | None = None,
        tunedModel_name: str | None = None,
        permission_id: str | int | None = None
) -> str:
    # resource_name is the name of the resource (corpus or tunedModel) for which the permission is being created.
    if name is None:
        # if name is not provided, then try to construct name via provided resource_name and permission_id.

        # only one type of resource_name can be provided.
        if corpus_name and tunedModel_name:
            raise ValueError(
                "Either `corpus_name` or `tunedModel_name` must be provided, not both."
            )
        
        resource_name = corpus_name or tunedModel_name
        resource_identifier = "corpora" if corpus_name else "tunedModels"

        if resource_name is None or permission_id is None:
            raise ValueError(
                "Either `name` or `resource_name` and `permission_id` must be provided."
            )
        else:
            if f"{resource_identifier}/" in resource_name:
                name = f"{resource_name}/"
            else:
                name = f"{resource_identifier}/{resource_name}/"
            
            if isinstance(permission_id, int) or "permissions/" not in permission_id:
                name += f"permissions/{permission_id}"

            else:
                name += permission_id

    # if name is provided, override resource_name and permission_id if provided.
    if not permission_types.valid_name(name):
        raise ValueError(
            f"Invalid name format. Expected format: \
                `(tunedModel|corpora)/<corpus_name>/permissions/<permission_id>`. Got: `{name}` instead."
        )
    return name

def get_permission(
    name: str | None = None,
    *,
    corpus_name: str | None = None,
    tunedModel_name: str | None = None,
    permission_id: str | int | None = None,
    client: glm.PermissionServiceClient | None = None,
) -> permission_types.Permission:
    """Get a permission by name.

    Args:
        name: The name of the permission.

    Returns:
        The permission as an instance of `permission_types.Permission`.
    """
    name = _construct_and_validate_name(name, corpus_name, tunedModel_name, permission_id)
    return permission_types.Permission.get(name=name, client=client)


async def get_permission_async(
    name: str | None = None,
    *,
    corpus_name: str | None = None,
    tunedModel_name: str | None = None,
    permission_id: str | int | None = None,
    client: glm.PermissionServiceAsyncClient | None = None,
) -> permission_types.Permission:
    """
    This is the async version of `permission.get_permission`.
    """
    name = _construct_and_validate_name(name, corpus_name, tunedModel_name, permission_id)
    return await permission_types.Permission.get_async(name=name, client=client)
