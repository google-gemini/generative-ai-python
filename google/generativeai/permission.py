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
    resource_name: str | None = None,
    permission_id: str | int | None = None,
    resource_type: str | None = None,
) -> str:
    # resource_name is the name of the supported resource (corpus or tunedModel as of now) for which the permission is being created.
    if not name:
        # if name is not provided, then try to construct name via provided resource_name and permission_id.
        if not (resource_name and permission_id):
            raise ValueError(
                "Either `name` or (`resource_name` and `permission_id`) must be provided."
            )

        if resource_type:
            resource_type = permission_types.to_resource_type(resource_type)
        else:
            # if resource_type is not provided, then try to infer it from resource_name.
            resource_path_components = resource_name.split("/")
            if len(resource_path_components) != 2:
                raise ValueError(
                    f"Invalid resource_name format. Expected format: `resource_type/resource_name`. Got: `{resource_name}` instead."
                )
            resource_type = permission_types.to_resource_type(resource_path_components[0])
        
        if f"{resource_type}/" in resource_name:
            name = f"{resource_name}/"
        else:
            name = f"{resource_type}/{resource_name}/"

        if isinstance(permission_id, int) or "permissions/" not in permission_id:
            name += f"permissions/{permission_id}"
        else:
            name += permission_id

    # if name is provided, override resource_name and permission_id if provided.
    if not permission_types.valid_name(name):
        raise ValueError(
            f"{permission_types.NAME_ERROR_MESSAGE}. Got: `{name}` instead."
        )
    return name


def get_permission(
    name: str | None = None,
    *,
    client: glm.PermissionServiceClient | None = None,
    resource_name: str | None = None,
    permission_id: str | int | None = None,
    resource_type: str | None = None,
) -> permission_types.Permission:
    """Get a permission by name.

    Args:
        name: The name of the permission.
        resource_name: The name of the supported resource for which the permission is being created.
        permission_id: The name of the permission.
        resource_type: The type of the resource (corpus or tunedModel as of now) for which the permission is being created. 
                        If not provided, it will be inferred from `resource_name`.

    Returns:
        The permission as an instance of `permission_types.Permission`.
    """
    name = _construct_and_validate_name(
        name=name,
        resource_name=resource_name,
        permission_id=permission_id,
        resource_type=resource_type
    )
    return permission_types.Permission.get(name=name, client=client)


async def get_permission_async(
    name: str | None = None,
    *,
    client: glm.PermissionServiceAsyncClient | None = None,
    resource_name: str | None = None,
    permission_id: str | int | None = None,
    resource_type: str | None = None,
) -> permission_types.Permission:
    """
    This is the async version of `permission.get_permission`.
    """
    name = _construct_and_validate_name(
        name=name,
        resource_name=resource_name,
        permission_id=permission_id,
        resource_type=resource_type
    )
    return await permission_types.Permission.get_async(name=name, client=client)
