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
import sys
from collections.abc import Iterable
import os
import unittest

from google.generativeai import client as client_lib
from google.generativeai import generative_models
import google.ai.generativelanguage as glm

from absl.testing import absltest
from absl.testing import parameterized


def simple_response(text: str) -> glm.GenerateContentResponse:
    return glm.GenerateContentResponse({"candidates": [{"content": {"parts": [{"text": text}]}}]})


class AsyncTests(parameterized.TestCase, unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = unittest.mock.MagicMock()

        client_lib._client_manager.clients["generative_async"] = self.client

        def add_client_method(f):
            name = f.__name__
            setattr(self.client, name, f)
            return f

        self.observed_requests = []
        self.responses = collections.defaultdict(list)

        @add_client_method
        async def generate_content(
            request: glm.GenerateContentRequest,
        ) -> glm.GenerateContentResponse:
            self.assertIsInstance(request, glm.GenerateContentRequest)
            self.observed_requests.append(request)
            response = self.responses["generate_content"].pop(0)
            return response

        @add_client_method
        async def stream_generate_content(
            request: glm.GetModelRequest,
        ) -> Iterable[glm.GenerateContentResponse]:
            self.observed_requests.append(request)
            response = self.responses["stream_generate_content"].pop(0)
            return response

    async def test_basic(self):
        # Generate text from text prompt
        model = generative_models.GenerativeModel(model_name="gemini-m")

        self.responses["generate_content"] = [simple_response("world!")]

        response = await model.generate_content_async("Hello")

        self.assertEqual(self.observed_requests[0].contents[0].parts[0].text, "Hello")
        self.assertEqual(response.candidates[0].content.parts[0].text, "world!")

        self.assertEqual(response.text, "world!")

    @unittest.skipIf(
        sys.version_info.major == 3 and sys.version_info.minor < 10,
        "streaming async requires python 3.10+",
    )
    async def test_streaming(self):
        # Generate text from text prompt
        model = generative_models.GenerativeModel(model_name="gemini-m")

        async def responses():
            for c in "world!":
                yield simple_response(c)

        self.responses["stream_generate_content"] = [responses()]

        response = await model.generate_content_async("Hello", stream=True)

        it = iter("world!")
        async for chunk in response:
            c = next(it)
            self.assertEqual(chunk.text, c)

        self.assertEqual(response.text, "world!")


if __name__ == "__main__":
    absltest.main()
