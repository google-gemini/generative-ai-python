import collections
from collections.abc import Iterable
import copy
import pathlib
from typing import Any
import textwrap
import unittest.mock
from absl.testing import absltest
from absl.testing import parameterized
import google.ai.generativelanguage as glm
from google.generativeai import client as client_lib
from google.generativeai import generative_models
from google.generativeai.types import content_types
from google.generativeai.types import generation_types

import PIL.Image


class SafetyTests(parameterized.TestCase):
    """Tests are in order with the design doc."""

    @parameterized.named_parameters(
        ["block_threshold", glm.SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE],
        ["block_threshold", "low"],
        ["block_threshold", 1],
        ["dict", {"danger": "low"}, {"danger": "high"}],
        [
            "list-dict",
            [
                dict(
                    category=glm.HarmCategory.HARM_CATEGORY_DANGEROUS,
                    threshold=glm.SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                ),
            ],
            ],[
            "list-dict2"
            [
                dict(category="danger", threshold="high"),
            ],
        ],
        [
            "object",
            [
                glm.SafetySetting(
                    category=glm.HarmCategory.HARM_CATEGORY_DANGEROUS,
                    threshold=glm.SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
                ),
            ],
        ],
    )
    def test_safety_overwrite(self, safe1, safe2):
        # Safety
        model = generative_models.GenerativeModel("gemini-pro", safety_settings=safe1)

        self.responses["generate_content"] = [
            simple_response(" world!"),
            simple_response(" world!"),
        ]

        _ = model.generate_content("hello")
        self.assertEqual(
            self.observed_requests[-1].safety_settings[0].category,
            glm.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        )
        self.assertEqual(
            self.observed_requests[-1].safety_settings[0].threshold,
            glm.SafetySetting.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
        )

        _ = model.generate_content("hello", safety_settings=safe2)
        self.assertEqual(
            self.observed_requests[-1].safety_settings[0].category,
            glm.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        )
        self.assertEqual(
            self.observed_requests[-1].safety_settings[0].threshold,
            glm.SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH,
        )


if __name__ == "__main__":
    absltest.main()
