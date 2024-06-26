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
import typing_extensions as typing


class UnitTests(absltest.TestCase):
    def test_controlled_generation(self):
        # [START controlled_generation]
        class Recipe(typing.TypedDict):
            recipe_name: str

        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        result = model.generate_content(
            "List a few popular cookie recipes.",
            generation_config=genai.GenerationConfig(
                response_mime_type="application/json", response_schema=list([Recipe])
            ),
        )
        print(result)
        print()
        # [END controlled_generation]


if __name__ == "__main__":
    absltest.main()
