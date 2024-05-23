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
import pathlib

from absl.testing import parameterized
import google.ai.generativelanguage as glm
from google.generativeai import responder

ROOT = pathlib.Path(__file__).parent.parent


class UnitTests(parameterized.TestCase):
    def test_check_glm_imports(self):
        for fpath in ROOT.rglob("*.py"):
            if fpath.name in [
                "client.py",
                "discuss.py",
                "test_protos.py",
                "test_client.py",
                "build_docs.py",
            ]:
                continue

            content = fpath.read_text()
            self.assertNotRegex(
                content,
                "import google\.ai\.generativelanguage|from google\.ai import generativelanguage",
                msg=f"generativelanguage found in {fpath}",
            )
