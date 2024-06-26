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
from google.generativeai import caching

import pathlib

media = pathlib.Path(__file__).parents[1] / "third_party"

class UnitTests(absltest.TestCase):
    def test_cache_create(self):
        # [START cache_create]
        document = genai.upload_file(path=media / "a11.txt")
        model_name = "gemini-1.5-flash-latest"
        cache = caching.CachedContent.create(
            model=model_name,
            system_instruction="You are an expert analyzing transcripts.",
            contents=[document]
        )
        print(cache)
        print()
        # [END cache_create]

    def test_cache_delete(self):
        # [START cache_delete]
        document = genai.upload_file(path=media / "a11.txt")
        model_name = "gemini-1.5-flash-latest"
        cache = caching.CachedContent.create(
            model=model_name,
            system_instruction="You are an expert analyzing transcripts.",
            contents=[document]
        )
        cache.delete()
        print()
        # [END cache_delete]

    def test_cache_get(self):
        # [START cache_get]
        document = genai.upload_file(path=media / "a11.txt")
        model_name = "gemini-1.5-flash-latest"
        cache = caching.CachedContent.create(
            model=model_name,
            system_instruction="You are an expert analyzing transcripts.",
            contents=[document]
        )
        print(cache.get(name=cache.name))
        print()
        # [END cache_get]

    def test_cache_list(self):
        # [START cache_list]
        document = genai.upload_file(path=media / "a11.txt")
        model_name = "gemini-1.5-flash-latest"
        cache = caching.CachedContent.create(
            model=model_name,
            system_instruction="You are an expert analyzing transcripts.",
            contents=[document]
        )
        print(cache.list())
        print()
        # [END cache_list]

    def test_cache_update(self):
        # [START cache_update]
        import datetime
        document = genai.upload_file(path=media / "a11.txt")
        model_name = "gemini-1.5-flash-latest"
        cache = caching.CachedContent.create(
            model=model_name,
            system_instruction="You are an expert analyzing transcripts.",
            contents=[document]
        )
        print(f"Before update:\n {cache}")
        print(cache)
        cache.update(ttl=datetime.timedelta(hours=2))
        print(f"After update:\n {cache}")
        print(cache)
        print()
        # [END cache_update]

if __name__ == "__main__":
    absltest.main()