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
from __future__ import annotations

import dataclasses
import pprint
import reprlib
import textwrap


def strip_oneof(docstring):
    lines = docstring.splitlines()
    lines = [line for line in lines if ".. _oneof:" not in line]
    lines = [line for line in lines if "This field is a member of `oneof`_" not in line]
    return "\n".join(lines)


def prettyprint(cls):
    cls.__str__ = _prettyprint
    cls.__repr__ = _prettyprint
    return cls



@reprlib.recursive_repr()
def _prettyprint(self):
    """You can't use `__str__ = pprint.pformat`. That causes a recursion error.

    This works, but it doesn't handle objects that reference themselves.
    """
    fields = []
    for f in dataclasses.fields(self):
        s = pprint.pformat(getattr(self, f.name))
        if s.count("\n") >= 10:
            s = "..."
        else:
            width = len(f.name) + 1
            s = textwrap.indent(s, " " * width).lstrip(" ")
        fields.append(f"{f.name}={s}")
    attrs = ",\n".join(fields)

    name = self.__class__.__name__
    width = len(name) + 1

    attrs = textwrap.indent(attrs, " " * width).lstrip(" ")
    return f"{name}({attrs})"
