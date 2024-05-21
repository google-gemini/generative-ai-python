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
#
# pytype: skip-file
r"""Api reference docs generation script, using tensorflow_docs

This script generates API reference docs for the reference doc generator.

$> pip install -U git+https://github.com/tensorflow/docs
$> python build_docs.py
"""

import os
import pathlib
import re
import textwrap
import typing


from absl import app
from absl import flags

import google
from google.ai import generativelanguage as glm

import grpc
import jinja2  # must be imported before turning on TYPE_CHECKING
import pydantic  # must be imported before turning on TYPE_CHECKING
from IPython import display  # must be imported before turning on TYPE_CHECKING
import PIL.Image  # must be imported before turning on TYPE_CHECKING

# For showing the conditional imports and types in `content_types.py`
# grpc must be imported first.
typing.TYPE_CHECKING = True
from google import generativeai as genai


from tensorflow_docs.api_generator import generate_lib

import yaml

HERE = pathlib.Path(__file__).parent

PROJECT_SHORT_NAME = "genai"
PROJECT_FULL_NAME = "Generative AI - Python"

_OUTPUT_DIR = flags.DEFINE_string(
    "output_dir",
    default=str(HERE / "api/"),
    help="Where to write the resulting docs to.",
)

_SEARCH_HINTS = flags.DEFINE_bool(
    "search_hints", True, "Include metadata search hints in the generated files"
)

_SITE_PATH = flags.DEFINE_string("site_path", "/api/python", "Path prefix in the _toc.yaml")

_CODE_URL_PREFIX = flags.DEFINE_string(
    "code_url_prefix",
    "https://github.com/google/generative-ai-python/blob/master/google/generativeai",
    "where to find the project code",
)


class MyFilter:
    def __init__(self, base_dirs):
        self.filter_base_dirs = public_api.FilterBaseDirs(base_dirs)

    def __call__(self, path, parent, children):
        if any("generativelanguage" in part for part in path) or "generativeai" in path:
            children = self.filter_base_dirs(path, parent, children)
            children = public_api.explicit_package_contents_filter(path, parent, children)

        return children


class MyDocGenerator(generate_lib.DocGenerator):
    def make_default_filters(self):
        return [
            # filter the api.
            public_api.FailIfNestedTooDeep(10),
            public_api.filter_module_all,
            public_api.add_proto_fields,
            public_api.filter_private_symbols,
            MyFilter(self._base_dir),  # Replaces: public_api.FilterBaseDirs(self._base_dir),
            public_api.FilterPrivateMap(self._private_map),
            public_api.filter_doc_controls_skip,
            public_api.ignore_typing,
        ]


def gen_api_docs():
    """Generates api docs for the generative-ai package."""
    for name in dir(google):
        if name not in ("generativeai", "ai"):
            delattr(google, name)
    google.__name__ = "google"
    google.__doc__ = textwrap.dedent(
        """\
        This is the top-level google namespace.
        """
    )

    doc_generator = generate_lib.DocGenerator(
        root_title=PROJECT_FULL_NAME,
        py_modules=[("google.generativeai", genai)],
        base_dir=(
            pathlib.Path(genai.__file__).parent,
            pathlib.Path(glm.__file__).parent.parent,
        ),
        code_url_prefix=(
            _CODE_URL_PREFIX.value,
            "https://github.com/googleapis/google-cloud-python/tree/main/packages/google-ai-generativelanguage/google/ai",
        ),
        search_hints=_SEARCH_HINTS.value,
        site_path=_SITE_PATH.value,
        callbacks=[],
    )

    out_path = pathlib.Path(_OUTPUT_DIR.value)
    doc_generator.build(out_path)

    # Fixup the toc file.
    toc_path = out_path / "google/_toc.yaml"
    toc = yaml.safe_load(toc_path.read_text())
    assert toc["toc"][0]["title"] == "google"
    toc["toc"] = toc["toc"][1:]
    toc["toc"][0]["title"] = "google.ai.generativelanguage"
    toc["toc"][0]["section"] = toc["toc"][0]["section"][1]["section"]
    toc["toc"][0], toc["toc"][1] = toc["toc"][1], toc["toc"][0]
    toc_path.write_text(yaml.dump(toc))

    # remove some dummy files and redirect them to `api/`
    (out_path / "google.md").unlink()
    (out_path / "google/ai.md").unlink()
    redirects_path = out_path / "_redirects.yaml"
    redirects = {"redirects": []}
    redirects["redirects"].insert(0, {"from": "/api/python/google/ai", "to": "/api/"})
    redirects["redirects"].insert(0, {"from": "/api/python/google", "to": "/api/"})
    redirects["redirects"].insert(0, {"from": "/api/python", "to": "/api/"})
    redirects_path.write_text(yaml.dump(redirects))

    # clear `oneof` junk from proto pages
    for fpath in out_path.rglob("*.md"):
        old_content = fpath.read_text()
        new_content = old_content
        new_content = re.sub(r"\.\. _oneof:.*?\n", "", new_content)
        new_content = re.sub(r".*?`oneof`_ ``_.*?\n", "", new_content, re.MULTILINE)
        new_content = re.sub(r"\.\. code-block:: python.*?\n", "", new_content)

        new_content = re.sub(r"generativelanguage_\w+\.types", "generativelanguage", new_content)

        if new_content != old_content:
            fpath.write_text(new_content)

    print("Output docs to: ", _OUTPUT_DIR.value)


def main(_):
    gen_api_docs()


if __name__ == "__main__":
    app.run(main)
