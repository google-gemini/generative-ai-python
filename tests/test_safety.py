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
from absl.testing import parameterized
from google.generativeai.types import safety_types
from google.generativeai import protos


class SafetyTests(parameterized.TestCase):
    """Tests are in order with the design doc."""

    @parameterized.named_parameters(
        ["block_threshold", protos.SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE],
        ["block_threshold2", "medium"],
        ["block_threshold3", 2],
        ["dict", {"danger": "medium"}],
        ["dict2", {"danger": 2}],
        ["dict3", {"danger": protos.SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE}],
        [
            "list-dict",
            [
                dict(
                    category=protos.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                    threshold=protos.SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                ),
            ],
        ],
        [
            "list-dict2",
            [
                dict(category="danger", threshold="med"),
            ],
        ],
    )
    def test_safety_overwrite(self, setting):
        setting = safety_types.to_easy_safety_dict(setting)
        self.assertEqual(
            setting[protos.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT],
            protos.SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        )


if __name__ == "__main__":
    absltest.main()
