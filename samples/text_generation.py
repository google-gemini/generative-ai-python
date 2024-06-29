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
import PIL.Image
from absl.testing import absltest

import google.generativeai as genai
import pathlib

media = pathlib.Path(__file__).parents[1] / "third_party"


class UnitTests(absltest.TestCase):
    def test_text_gen_text_only_prompt(self):
        # [START text_gen_text_only_prompt]
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Give me python code to sort a list")
        print(response.text)
        # [END text_gen_text_only_prompt]

    def test_text_gen_text_only_prompt_streaming(self):
        # [START text_gen_text_only_prompt_streaming]
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Give me python code to sort a list", stream=True)
        for chunk in response:
            print(chunk.text)
            print("_" * 80)
        # [END text_gen_text_only_prompt_streaming]

    def test_text_gen_multimodal_one_image_prompt(self):
        # [START text_gen_multimodal_one_image_prompt]
        import PIL

        model = genai.GenerativeModel("gemini-1.5-flash")
        organ = PIL.Image.open(media / "organ.jpg")
        response = model.generate_content(["Tell me about this instrument", organ])
        print(response.text)
        # [END text_gen_multimodal_one_image_prompt]

    def test_text_gen_multimodal_one_image_prompt_streaming(self):
        # [START text_gen_multimodal_one_image_prompt_streaming]
        import PIL

        model = genai.GenerativeModel("gemini-1.5-flash")
        organ = PIL.Image.open(media / "organ.jpg")
        response = model.generate_content(["Tell me about this instrument", organ], stream=True)
        for chunk in response:
            print(chunk.text)
            print("_" * 80)
        # [END text_gen_multimodal_one_image_prompt_streaming]

    def test_text_gen_multimodal_multi_image_prompt(self):
        # [START text_gen_multimodal_multi_image_prompt]
        import PIL

        model = genai.GenerativeModel("gemini-1.5-flash")
        organ = PIL.Image.open(media / "organ.jpg")
        cajun_instrument = PIL.Image.open(media / "Cajun_instruments.jpg")
        response = model.generate_content(
            ["What is the difference between both of these instruments?", organ, cajun_instrument]
        )
        print(response.text)
        # [END text_gen_multimodal_multi_image_prompt]

    def test_text_gen_multimodal_multi_image_prompt_streaming(self):
        # [START text_gen_multimodal_multi_image_prompt_streaming]
        import PIL

        model = genai.GenerativeModel("gemini-1.5-flash")
        organ = PIL.Image.open(media / "organ.jpg")
        cajun_instrument = PIL.Image.open(media / "Cajun_instruments.jpg")
        response = model.generate_content(
            ["What is the difference between both of these instruments?", organ, cajun_instrument],
            stream=True,
        )
        for chunk in response:
            print(chunk.text)
            print("_" * 80)
        # [END text_gen_multimodal_multi_image_prompt_streaming]

    def test_text_gen_multimodal_audio(self):
        # [START text_gen_multimodal_audio]
        model = genai.GenerativeModel("gemini-1.5-flash")
        sample_audio = genai.upload_file(media / "sample.mp3")
        response = model.generate_content(["Give me a summary of this audio file.", sample_audio])
        print(response.text)
        # [END text_gen_multimodal_audio]

    def test_text_gen_multimodal_video_prompt(self):
        # [START text_gen_multimodal_video_prompt]
        model = genai.GenerativeModel("gemini-1.5-flash")
        video = genai.upload_file(media / "Big_Buck_Bunny.mp4")
        response = model.generate_content(["Describe this video clip.", video])
        print(response.text)
        # [END text_gen_multimodal_video_prompt]

    def test_text_gen_multimodal_video_prompt_streaming(self):
        # [START text_gen_multimodal_video_prompt_streaming]
        model = genai.GenerativeModel("gemini-1.5-flash")
        video = genai.upload_file(media / "Big_Buck_Bunny.mp4")
        response = model.generate_content(["Describe this video clip.", video], stream=True)
        for chunk in response:
            print(chunk.text)
            print("_" * 80)
        # [END text_gen_multimodal_video_prompt_streaming]


if __name__ == "__main__":
    absltest.main()
