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
from absl.testing import absltest

import google.generativeai as genai


class UnitTests(absltest.TestCase):
    def test_code_execution_basic(self):
        # [START code_execution_basic]
        model = genai.GenerativeModel(model_name="gemini-1.5-flash", tools="code_execution")
        result = model.generate_content(
            "What's the sum of the sum of first 200 prime numbers? Make sure you get all 200."
        )
        print(result.text)
        # [END code_execution_basic]

    def test_code_execution_request_override(self):
        # [START code_execution_request_override]
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        result = model.generate_content(
            "Write code to count how many letter r in the word strawberry", tools="code_execution"
        )
        print(result.text)
        # [END code_execution_request_override]

    def test_code_execution_chat(self):
        # [START code_execution_chat]
        model = genai.GenerativeModel(model_name="gemini-1.5-flash", tools="code_execution")
        chat = model.start_chat()
        result = chat.send_message(
            "Can you run some code to bogo-sort this list of numbers?: [2,34,1,65,4]"
        )
        print(result.text)
        # [END code_execution_chat]


if __name__ == "__main__":
    absltest.main()
