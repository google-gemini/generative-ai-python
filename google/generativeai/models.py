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

import re
from typing import Optional, List, Iterator

import google.ai.generativelanguage as glm
from google.generativeai.client import get_default_model_client
from google.generativeai.types import model_types


def get_model(name: str, *, client=None) -> model_types.Model:
    """Get the `types.Model` for the given model name."""
    if client is None:
        client = get_default_model_client()

    name = model_types.make_model_name(name)

    result = client.get_model(name=name)
    result = type(result).to_dict(result)
    return model_types.Model(**result)


class ModelsIterable(model_types.ModelsIterable):
    """
    An iterable class to traverse through a list of models.

    This class allows you to iterate over a list of models, fetching them in pages
    if necessary based on the provided `page_size` and `page_token`.

    Args:
        page_size: The number of `models` to fetch per page.
        page_token: Token representing the current page. Pass `None` for the first page.
        models: List of models to iterate through.
        client: An optional client for the model service.

    Returns:
        A `ModelsIterable` iterable object that allows iterating through the models.
    """

    def __init__(
        self,
        *,
        page_size: int,
        page_token: str | None,
        models: List[model_types.Model],
        client: glm.ModelServiceClient | None,
    ):
        self._page_size = page_size
        self._page_token = page_token
        self._models = models
        self._client = client

    def __iter__(self) -> Iterator[model_types.Model]:
        """
        Returns an iterator over the models.
        """
        while self:
            page = self._models
            yield from page
            self = self._next_page()

    def _next_page(self) -> ModelsIterable | None:
        """
        Fetches the next page of models based on the page token.
        """
        if not self._page_token:
            return None
        return _list_models(
            page_size=self._page_size, page_token=self._page_token, client=self._client
        )


def _list_models(
    page_size: int, page_token: str | None, client: glm.ModelServiceClient
) -> ModelsIterable:
    """
    Fetches a page of models using the provided client and pagination tokens.

    This function queries the `client` to retrieve a page of models based on the given
    `page_size` and `page_token`. It then processes the response and returns an iterable
    object to traverse through the models.

    Args:
        page_size: How many `types.Models` to fetch per page (api call).
        page_token: Token representing the current page.
        client: The client to communicate with the model service.

    Returns:
        An iterable `ModelsIterable` object containing the fetched models and pagination info.
    """
    result = client.list_models(page_size=page_size, page_token=page_token)
    result = result._response
    result = type(result).to_dict(result)

    result["models"] = [model_types.Model(**mod) for mod in result["models"]]
    result["page_size"] = page_size
    result["page_token"] = result.pop("next_page_token")
    result["client"] = client
    return ModelsIterable(**result)


def list_models(
    *, page_size: int | None = None, client: glm.ModelServiceClient | None = None
) -> model_types.ModelsIterable:
    """Lists available models.

    ```
    import pprint
    for model in genai.list_models():
        pprint.pprint(model)
    ```

    Args:
        page_size: How many `types.Models` to fetch per page (api call).
        client: You may pass a `glm.ModelServiceClient` instead of using the default client.

    Returns:
        An iterable of `types.Model` objects.

    """
    if client is None:
        client = get_default_model_client()

    return _list_models(page_size, page_token=None, client=client)
