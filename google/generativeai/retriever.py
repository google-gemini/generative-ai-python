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
import string
import dataclasses
from typing import Optional

import google.ai.generativelanguage as glm

from google.generativeai.client import get_default_retriever_client
from google.generativeai.client import get_default_retriever_async_client
from google.generativeai import string_utils
from google.generativeai.types import retriever_types
from google.generativeai.types import model_types
from google.generativeai import models
from google.generativeai.types import safety_types
from google.generativeai.types.model_types import idecode_time

_CORPORA_NAME_REGEX = re.compile(r"^corpora/[a-z0-9-]+")
_REMOVE = string.punctuation
_REMOVE = _REMOVE.replace("-", "")  # Don't remove hyphens
_PATTERN = r"[{}]".format(_REMOVE)  # Create the pattern


@string_utils.prettyprint
@dataclasses.dataclass(init=False)
class Corpus(retriever_types.Corpus):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.result = None
        if self.name:
            self.result = self.name


def create_corpus(
    name: Optional[str] = None,
    display_name: Optional[str] = None,
    client: glm.RetrieverServiceClient | None = None,
) -> Corpus:
    """
    Create a Corpus object. Users can specify either a name or display_name.

    Args:
        name: The corpus resource name (ID). The name must be alphanumeric and fewer
            than 40 characters.
        display_name: The human readable display name. The display name must be fewer
            than 128 characters. All characters, including alphanumeric, spaces, and
            dashes are supported.

    Return:
        Corpus object with specified name or display name.

    Raises:
        ValueError: When the name is not specified or formatted incorrectly.
    """
    if client is None:
        client = get_default_retriever_client()

    if not name and not display_name:
        raise ValueError("Either the corpus name or display name must be specified.")

    corpus = None
    if name:
        if re.match(_CORPORA_NAME_REGEX, name):
            corpus = glm.Corpus(name=name, display_name=display_name)
        elif "corpora/" not in name:
            corpus_name = "corpora/" + re.sub(_PATTERN, "", name)
            corpus = glm.Corpus(name=corpus_name, display_name=display_name)
        else:
            raise ValueError("Corpus name must be formatted as corpora/<corpus_name>.")

    request = glm.CreateCorpusRequest(corpus=corpus)
    response = client.create_corpus(request)
    response = type(response).to_dict(response)
    idecode_time(response, "create_time")
    idecode_time(response, "update_time")
    response = Corpus(**response)
    return response


async def create_corpus_async(
    name: Optional[str] = None,
    display_name: Optional[str] = None,
    client: glm.RetrieverServiceAsyncClient | None = None,
) -> Corpus:
    """This is the async version of `create_corpus`."""
    if client is None:
        client = get_default_retriever_async_client()

    if not name and not display_name:
        raise ValueError("Either the corpus name or display name must be specified.")

    corpus = None
    if name:
        if re.match(_CORPORA_NAME_REGEX, name):
            corpus = glm.Corpus(name=name, display_name=display_name)
        elif "corpora/" not in name:
            corpus_name = "corpora/" + re.sub(_PATTERN, "", name)
            corpus = glm.Corpus(name=corpus_name, display_name=display_name)
        else:
            raise ValueError("Corpus name must be formatted as corpora/<corpus_name>.")

    request = glm.CreateCorpusRequest(corpus=corpus)
    response = await client.create_corpus(request)
    response = type(response).to_dict(response)
    idecode_time(response, "create_time")
    idecode_time(response, "update_time")
    response = Corpus(**response)
    return response


def get_corpus(name: str, client: glm.RetrieverServiceClient | None = None) -> Corpus:  # fmt: skip
    """
    Get information about a specific `Corpus`.

    Args:
        name: The `Corpus` name.

    Return:
        `Corpus` of interest.
    """
    if client is None:
        client = get_default_retriever_client()

    request = glm.GetCorpusRequest(name=name)
    response = client.get_corpus(request)
    response = type(response).to_dict(response)
    idecode_time(response, "create_time")
    idecode_time(response, "update_time")
    response = Corpus(**response)
    return response


async def get_corpus_async(name: str, client: glm.RetrieverServiceAsyncClient | None = None) -> Corpus:  # fmt: skip
    """This is the async version of `get_corpus`."""
    if client is None:
        client = get_default_retriever_async_client()

    request = glm.GetCorpusRequest(name=name)
    response = await client.get_corpus(request)
    response = type(response).to_dict(response)
    idecode_time(response, "create_time")
    idecode_time(response, "update_time")
    response = Corpus(**response)
    return response


def delete_corpus(name: str, force: bool, client: glm.RetrieverServiceClient | None = None):  # fmt: skip
    """
    Delete a `Corpus`.

    Args:
        name: The `Corpus` name.
        force: If set to true, any `Document`s and objects related to this `Corpus` will also be deleted.
    """
    if client is None:
        client = get_default_retriever_client()

    request = glm.DeleteCorpusRequest(name=name, force=force)
    client.delete_corpus(request)


async def delete_corpus_async(name: str, force: bool, client: glm.RetrieverServiceAsyncClient | None = None):  # fmt: skip
    """This is the async version of `delete_corpus`."""
    if client is None:
        client = get_default_retriever_async_client()

    request = glm.DeleteCorpusRequest(name=name, force=force)
    await client.delete_corpus(request)


def list_corpora(
    *,
    page_size: Optional[int] = None,
    page_token: Optional[str] = None,
    client: glm.RetrieverServiceClient | None = None,
) -> list[Corpus]:
    """
    List `Corpus`.

    Args:
        page_size: Maximum number of `Corpora` to request.
        page_token: A page token, received from a previous ListCorpora call.

    Return:
        Paginated list of `Corpora`.
    """
    if client is None:
        client = get_default_retriever_client()

    request = glm.ListCorporaRequest(page_size=page_size, page_token=page_token)
    response = client.list_corpora(request)
    return response


async def list_corpora_async(
    *,
    page_size: Optional[int] = None,
    page_token: Optional[str] = None,
    client: glm.RetrieverServiceClient | None = None,
) -> list[Corpus]:
    """This is the async version of `list_corpora`."""
    if client is None:
        client = get_default_retriever_async_client()

    request = glm.ListCorporaRequest(page_size=page_size, page_token=page_token)
    response = await client.list_corpora(request)
    return response
