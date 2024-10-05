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

import collections
from collections.abc import Iterable
import io
import os
from typing import Any, Iterable, Sequence
import unittest
import asyncio

from google.generativeai import client as client_lib
from google.generativeai import protos
from google.generativeai import files

from absl.testing import parameterized

class AsyncFileServiceClient(client_lib.FileServiceClient):
    async def __init__(self, test):
        self.test = test
        self.observed_requests = []
        self.responses = collections.defaultdict(list)

    async def create_file_async(
        self,
        path: str | io.IOBase | os.PathLike,
        *,
        mime_type: str | None = None,
        name: str | None = None,
        display_name: str | None = None,
        resumable: bool = True,
        metadata: Sequence[tuple[str, str]] = (),
    ) -> protos.File:
        self.observed_requests.append(
            dict(
                path=path,
                mime_type=mime_type,
                name=name,
                display_name=display_name,
                resumable=resumable,
            )
        )
        return self.responses["create_file"].pop(0)

    async def get_file_async(
        self,
        request: protos.GetFileRequest,
        **kwargs,
    ) -> protos.File:
        self.observed_requests.append(request)
        return self.responses["get_file"].pop(0)

    def list_files(
        self,
        request: protos.ListFilesRequest,
        **kwargs,
    ) -> Iterable[protos.File]:
        self.observed_requests.append(request)
        for f in self.responses["list_files"].pop(0):
            yield f

    def delete_file(
        self,
        request: protos.DeleteFileRequest,
        **kwargs,
    ):
        self.observed_requests.append(request)
        return

class AsyncTests(parameterized.TestCase, unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = FileServiceClient(self)

        client_lib._client_manager.clients["file"] = self.client