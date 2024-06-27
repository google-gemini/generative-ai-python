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
import pathlib

media = pathlib.Path(__file__).parents[1] / "third_party"

class UnitTests(absltest.TestCase):
    def test_tokens_text_only(self):
        # [START tokens_text_only]
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        print(model.count_tokens("The quick brown fox jumps over the lazy dog."))
        # [END tokens_text_only]

    def test_tokens_chat(self):
        # [START tokens_chat]
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        chat = model.start_chat(history=[{'role':'user', 
                                          'parts':'Hi, my name is Bob.'},  
                                        {'role':'model', 
                                         'parts':'Hi Bob!'}])
        model.count_tokens(chat.history)

        from google.generativeai.types.content_types import to_contents
        model.count_tokens(chat.history + to_contents('What is the meaning of life?'))
        # [END tokens_chat]

    def test_tokens_multimodal_image_inline(self):
        # [START tokens_multimodal_image_inline]
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        import PIL
        organ = PIL.Image.open(media / 'organ.jpg')
        print(model.count_tokens(['Tell me about this instrument', organ]))
        # [END tokens_multimodal_image_inline]

    def test_tokens_multimodal_image_file_api(self):
        # [START tokens_multimodal_image_file_api]
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        organ_upload = genai.upload_file(media / 'organ.jpg')
        print(model.count_tokens(['Tell me about this instrument', organ_upload]))
        # [END tokens_multimodal_image_file_api]

    def test_tokens_video_audio_file_api(self):
        # [START tokens_video_audio_file_api]
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        audio_upload = genai.upload_file(media / 'sample.mp3')
        print(model.count_tokens(audio_upload))
        # [END tokens_video_audio_file_api]

    def test_tokens_cached_content(self):
        # [START tokens_cached_content]
        # [END tokens_cached_content]

    def test_tokens_cached_system_instruction(self):
        # [START tokens_cached_system_instruction]
        print(genai.GenerativeModel().count_tokens("The quick brown fox jumps over the lazy dog."))
        print(genai.GenerativeModel(
            system_instruction='Talk like a pirate!'
            ).count_tokens(
                "The quick brown fox jumps over the lazy dog."
                ))
        # [END tokens_cached_system_instruction]

    def test_tokens_cached_tools(self):
        # [START tokens_cached_tools]
        # [END tokens_cached_tools]

if __name__ == "__main__":
    absltest.main()