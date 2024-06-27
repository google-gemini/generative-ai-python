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
    def test_tokens_text_only(self):
        # [START tokens_text_only]
        # [END tokens_text_only]

    def test_tokens_chat(self):
        # [START tokens_chat]
        # [END tokens_chat]

    def test_tokens_multimodal_image_inline(self):
        # [START tokens_multimodal_image_inline]
        # [END tokens_multimodal_image_inline]

    def test_tokens_multimodal_image_file_api(self):
        # [START tokens_multimodal_image_file_api]
        # [END tokens_multimodal_image_file_api]

    def test_tokens_video_audio_file_api(self):
        # [START tokens_video_audio_file_api]
        # [END tokens_video_audio_file_api]

    def test_tokens_multimodal_image_inline(self):
        # [START tokens_multimodal_image_inline]
        # [END tokens_multimodal_image_inline]

    def test_count_tokens_and_usage_metadata(self):
        # [START count_tokens_and_usage_metadata]
        # [END count_tokens_and_usage_metadata]

if __name__ == "__main__":
    absltest.main()