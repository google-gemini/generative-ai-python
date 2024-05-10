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
from google.generativeai.types import safety_types
from google.generativeai.types import generation_types

import PIL.Image


class SafetyTests(parameterized.TestCase):
    """Tests are in order with the design doc."""

    @parameterized.named_parameters(
        ["block_threshold", glm.SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE],
        ["block_threshold2", "medium"],
        ["block_threshold3", 2],
        ["dict", {"danger": "medium"}],
        ["dict2", {"danger": 2}],
        ["dict3", {"danger": glm.SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE}],
        [
            "list-dict",
            [
                dict(
                    category=glm.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                    threshold=glm.SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
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
        setting = safety_types.to_easy_safety_dict(setting, "new")
        self.assertEqual(
            setting[glm.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT],
            glm.SafetySetting.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        )


if __name__ == "__main__":
    absltest.main()
