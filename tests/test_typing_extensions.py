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
import re

from absl.testing import absltest

TYPING_RE = re.compile(r"\btyping\b.*TypedDict")


class TypingExtensionsTests(absltest.TestCase):
    """Pydantic users need the improved version of TypedDict, from typing_extensions.

    This is only required for python versions <3.12. Once 3.12 is the lowest supported version we can drop this.

    ref: https://docs.pydantic.dev/2.3/usage/types/dicts_mapping/

    > the typing-extensions package is required for Python <3.12
    """

    def test_no_typing_typed_dict(self):
        root = pathlib.Path(__file__).parent.parent
        for fpath in (root / "google").rglob("*.py"):
            source = fpath.read_text()
            if match := TYPING_RE.search(source):
                raise ValueError(
                    f"Please import `TypedDict` from `typing_extensions` not `typing`, in:", fpath
                )


if __name__ == "__main__":
    absltest.main()
