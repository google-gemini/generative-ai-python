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

import os
import unittest
import unittest.mock as mock

import google.ai.generativelanguage as glm

from google.generativeai import text as text_service
from google.generativeai import client
from absl.testing import absltest
from absl.testing import parameterized


class UnitTests(parameterized.TestCase):
    def setUp(self):
        self.client = unittest.mock.MagicMock()

        client.default_text_client = self.client

        self.observed_request = None

        def fake_generate_completion(
            request: glm.GenerateTextRequest,
        ) -> glm.GenerateTextResponse:
            self.observed_request = request
            return glm.GenerateTextResponse(
                candidates=[
                    glm.TextCompletion(output=" road?"),
                    glm.TextCompletion(output=" bridge?"),
                    glm.TextCompletion(output=" river?"),
                ]
            )

        self.client.generate_text = fake_generate_completion

        def fake_embed_text(
            request: glm.EmbedTextRequest,
        ) -> glm.EmbedTextResponse:
            self.observed_request = request
            return glm.EmbedTextResponse(embedding=glm.Embedding(value=[1, 2, 3]))

        self.client.embed_text = fake_embed_text

    @parameterized.named_parameters(
        [
            dict(testcase_name="string", prompt="Hello how are"),
        ]
    )
    def test_make_prompt(self, prompt):
        x = text_service._make_text_prompt(prompt)
        self.assertIsInstance(x, glm.TextPrompt)
        self.assertEqual("Hello how are", x.text)

    @parameterized.named_parameters(
        [
            dict(testcase_name="string", prompt="What are you"),
        ]
    )
    def test_make_generate_text_request(self, prompt):
        x = text_service._make_generate_text_request(prompt=prompt)
        self.assertEqual("models/chat-lamda-001", x.model)
        self.assertIsInstance(x, glm.GenerateTextRequest)

    # @unittest.skipUnless(os.getenv('API_KEY'), "No API key set")
    @parameterized.named_parameters(
        [
            dict(
                testcase_name="basic_model",
                model="models/chat-lamda-001",
                text="What are you",
            )
        ]
    )
    def test_generate_embeddings(self, model, text):
        emb = text_service.generate_embeddings(model=model, text=text)

        self.assertIsInstance(emb, dict)
        self.assertEqual(
            self.observed_request, glm.EmbedTextRequest(model=model, text=text)
        )

    @parameterized.named_parameters(
        [
            dict(testcase_name="basic", prompt="Why did the chicken cross the"),
            dict(
                testcase_name="temperature",
                prompt="Why did the chicken cross the",
                temperature=0.75,
            ),
            dict(
                testcase_name="stop_list",
                prompt="Why did the chicken cross the",
                stop_sequences=["a", "b", "c"],
            ),
            dict(
                testcase_name="count",
                prompt="Why did the chicken cross the",
                candidate_count=2,
            ),
        ]
    )
    def test_generate_response(self, *, prompt, **kwargs):
        complete = text_service.generate_text(prompt=prompt, **kwargs)

        self.assertEqual(
            self.observed_request,
            glm.GenerateTextRequest(
                model="models/text-bison-001",
                prompt=glm.TextPrompt(text=prompt),
                **kwargs
            ),
        )

        self.assertIsInstance(complete.result, str)

        self.assertEqual(
            complete.candidates,
            [
                {"output": " road?", 'safety_ratings': []},
                {"output": " bridge?", 'safety_ratings': []},
                {"output": " river?", 'safety_ratings': []},
            ],
        )

    def test_stop_string(self):
        complete = text_service.generate_text(prompt="Hello", stop_sequences="stop")

        self.assertEqual(
            self.observed_request,
            glm.GenerateTextRequest(
                model="models/text-bison-001",
                prompt=glm.TextPrompt(text="Hello"),
                stop_sequences=["stop"],
            ),
        )


if __name__ == "__main__":
    absltest.main()
