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

import os
from typing import cast, Optional, Union

import google.ai.generativelanguage as glm

from google.auth import credentials as ga_credentials
from google.api_core import client_options as client_options_lib
from google.api_core import gapic_v1
from google.api_core import operations_v1

from google.generativeai import version


USER_AGENT = "genai-py"

default_client_config = {}
default_discuss_client = None
default_discuss_async_client = None
default_model_client = None
default_text_client = None
default_operations_client = None


def configure(
    *,
    api_key: str | None = None,
    credentials: ga_credentials.Credentials | dict | None = None,
    # The user can pass a string to choose `rest` or `grpc` or 'grpc_asyncio'.
    # See `_transport_registry` in `DiscussServiceClientMeta`.
    # Since the transport classes align with the client classes it wouldn't make
    # sense to accept a `Transport` object here even though the client classes can.
    # We could accept a dict since all the `Transport` classes take the same args,
    # but that seems rare. Users that need it can just switch to the low level API.
    transport: str | None = None,
    client_options: client_options_lib.ClientOptions | dict | None = None,
    client_info: gapic_v1.client_info.ClientInfo | None = None,
):
    """Captures default client configuration.

    If no API key has been provided (either directly, or on `client_options`) and the
    `GOOGLE_API_KEY` environment variable is set, it will be used as the API key.

    Args:
        Refer to `glm.DiscussServiceClient`, and `glm.ModelsServiceClient` for details on additional arguments.
        api_key: The API-Key to use when creating the default clients (each service uses
            a separate client). This is a shortcut for `client_options={"api_key": api_key}`.
            If omitted, and the `GOOGLE_API_KEY` environment variable is set, it will be
            used.
    """
    global default_client_config
    global default_discuss_client
    global default_model_client
    global default_text_client
    global default_operations_client

    if isinstance(client_options, dict):
        client_options = client_options_lib.from_dict(client_options)
    if client_options is None:
        client_options = client_options_lib.ClientOptions()
    client_options = cast(client_options_lib.ClientOptions, client_options)
    had_api_key_value = getattr(client_options, "api_key", None)

    if had_api_key_value:
        if api_key is not None:
            raise ValueError(
                "You can't set both `api_key` and `client_options['api_key']`."
            )
    else:
        if api_key is None:
            # If no key is provided explicitly, attempt to load one from the
            # environment.
            api_key = os.getenv("GOOGLE_API_KEY")

        client_options.api_key = api_key

    user_agent = f"{USER_AGENT}/{version.__version__}"
    if client_info:
        # Be respectful of any existing agent setting.
        if client_info.user_agent:
            client_info.user_agent += f" {user_agent}"
        else:
            client_info.user_agent = user_agent
    else:
        client_info = gapic_v1.client_info.ClientInfo(user_agent=user_agent)

    new_default_client_config = {
        "credentials": credentials,
        "transport": transport,
        "client_options": client_options,
        "client_info": client_info,
    }

    new_default_client_config = {
        key: value
        for key, value in new_default_client_config.items()
        if value is not None
    }

    default_client_config = new_default_client_config
    default_discuss_client = None
    default_text_client = None
    default_model_client = None
    default_operations_client = None


def get_default_discuss_client() -> glm.DiscussServiceClient:
    global default_discuss_client
    if default_discuss_client is None:
        # Attempt to configure using defaults.
        if not default_client_config:
            configure()
        default_discuss_client = glm.DiscussServiceClient(**default_client_config)

    return default_discuss_client


def get_default_text_client() -> glm.TextServiceClient:
    global default_text_client
    if default_text_client is None:
        # Attempt to configure using defaults.
        if not default_client_config:
            configure()
        default_text_client = glm.TextServiceClient(**default_client_config)

    return default_text_client


def get_default_discuss_async_client() -> glm.DiscussServiceAsyncClient:
    global default_discuss_async_client
    if default_discuss_async_client is None:
        # Attempt to configure using defaults.
        if not default_client_config:
            configure()
        default_discuss_async_client = glm.DiscussServiceAsyncClient(
            **default_client_config
        )

    return default_discuss_async_client


def get_default_model_client() -> glm.ModelServiceClient:
    global default_model_client
    if default_model_client is None:
        # Attempt to configure using defaults.
        if not default_client_config:
            configure()
        default_model_client = glm.ModelServiceClient(**default_client_config)

    return default_model_client


def get_default_operations_client() -> operations_v1.OperationsClient:
    global default_operations_client
    if default_operations_client is None:
        model_client = get_default_model_client()
        default_operations_client = model_client._transport.operations_client

    return default_operations_client
