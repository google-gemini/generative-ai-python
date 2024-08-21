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
    def test_json_controlled_generation(self):
        # [START json_controlled_generation]
        import typing_extensions as typing

        class Recipe(typing.TypedDict):
            recipe_name: str

        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        result = model.generate_content(
            "List a few popular cookie recipes.",
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json", response_schema=list[Recipe]
            ),
        )
        print(result)
        # [END json_controlled_generation]

    def test_json_no_schema(self):
        # [START json_no_schema]
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        prompt = """List a few popular cookie recipes using this JSON schema:

        Recipe = {'recipe_name': str}
        Return: list[Recipe]"""
        result = model.generate_content(prompt)
        print(result)
        # [END json_no_schema]


if __name__ == "__main__":
    absltest.main()
