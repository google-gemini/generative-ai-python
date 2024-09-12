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
from typing import Any

from absl.testing import absltest
from absl.testing import parameterized
from google.generativeai import protos
from google.generativeai import responder


HERE = pathlib.Path(__file__).parent
TEST_PNG_PATH = HERE / "test_img.png"
TEST_PNG_URL = "https://storage.googleapis.com/generativeai-downloads/data/test_img.png"
TEST_PNG_DATA = TEST_PNG_PATH.read_bytes()

TEST_JPG_PATH = HERE / "test_img.jpg"
TEST_JPG_URL = "https://storage.googleapis.com/generativeai-downloads/data/test_img.jpg"
TEST_JPG_DATA = TEST_JPG_PATH.read_bytes()


# simple test function
def datetime():
    "Returns the current UTC date and time."


class UnitTests(parameterized.TestCase):
    @parameterized.named_parameters(
        [
            "FunctionLibrary",
            responder.FunctionLibrary(
                tools=protos.Tool(
                    function_declarations=[
                        protos.FunctionDeclaration(
                            name="datetime", description="Returns the current UTC date and time."
                        )
                    ]
                )
            ),
        ],
        [
            "IterableTool-Tool",
            [
                responder.Tool(
                    function_declarations=[
                        protos.FunctionDeclaration(
                            name="datetime", description="Returns the current UTC date and time."
                        )
                    ]
                )
            ],
        ],
        [
            "IterableTool-protos.Tool",
            [
                protos.Tool(
                    function_declarations=[
                        protos.FunctionDeclaration(
                            name="datetime",
                            description="Returns the current UTC date and time.",
                        )
                    ]
                )
            ],
        ],
        [
            "IterableTool-ToolDict",
            [
                dict(
                    function_declarations=[
                        dict(
                            name="datetime",
                            description="Returns the current UTC date and time.",
                        )
                    ]
                )
            ],
        ],
        [
            "IterableTool-IterableFD",
            [
                [
                    protos.FunctionDeclaration(
                        name="datetime",
                        description="Returns the current UTC date and time.",
                    )
                ]
            ],
        ],
        [
            "IterableTool-FD",
            [
                protos.FunctionDeclaration(
                    name="datetime",
                    description="Returns the current UTC date and time.",
                )
            ],
        ],
        [
            "Tool",
            responder.Tool(
                function_declarations=[
                    protos.FunctionDeclaration(
                        name="datetime", description="Returns the current UTC date and time."
                    )
                ]
            ),
        ],
        [
            "protos.Tool",
            protos.Tool(
                function_declarations=[
                    protos.FunctionDeclaration(
                        name="datetime", description="Returns the current UTC date and time."
                    )
                ]
            ),
        ],
        [
            "ToolDict",
            dict(
                function_declarations=[
                    dict(name="datetime", description="Returns the current UTC date and time.")
                ]
            ),
        ],
        [
            "IterableFD-FD",
            [
                responder.FunctionDeclaration(
                    name="datetime", description="Returns the current UTC date and time."
                )
            ],
        ],
        [
            "IterableFD-CFD",
            [
                responder.CallableFunctionDeclaration(
                    name="datetime",
                    description="Returns the current UTC date and time.",
                    function=datetime,
                )
            ],
        ],
        [
            "IterableFD-dict",
            [dict(name="datetime", description="Returns the current UTC date and time.")],
        ],
        ["IterableFD-Callable", [datetime]],
        [
            "FD",
            responder.FunctionDeclaration(
                name="datetime", description="Returns the current UTC date and time."
            ),
        ],
        [
            "CFD",
            responder.CallableFunctionDeclaration(
                name="datetime",
                description="Returns the current UTC date and time.",
                function=datetime,
            ),
        ],
        [
            "protos.FD",
            protos.FunctionDeclaration(
                name="datetime", description="Returns the current UTC date and time."
            ),
        ],
        ["dict", dict(name="datetime", description="Returns the current UTC date and time.")],
        ["Callable", datetime],
    )
    def test_to_tools(self, tools):
        function_library = responder.to_function_library(tools)
        if function_library is None:
            raise ValueError("This shouldn't happen")
        tools = function_library.to_proto()

        tools = type(tools[0]).to_dict(tools[0])
        tools["function_declarations"][0].pop("parameters", None)

        expected = dict(
            function_declarations=[
                dict(name="datetime", description="Returns the current UTC date and time.")
            ]
        )

        self.assertEqual(tools, expected)

    def test_two_fun_is_one_tool(self):
        def a():
            pass

        def b():
            pass

        function_library = responder.to_function_library([a, b])
        if function_library is None:
            raise ValueError("This shouldn't happen")
        tools = function_library.to_proto()

        self.assertLen(tools, 1)
        self.assertLen(tools[0].function_declarations, 2)

    @parameterized.named_parameters(
        ["int", int, protos.Schema(type=protos.Type.INTEGER)],
        ["float", float, protos.Schema(type=protos.Type.NUMBER)],
        ["str", str, protos.Schema(type=protos.Type.STRING)],
        [
            "list",
            list[str],
            protos.Schema(
                type=protos.Type.ARRAY,
                items=protos.Schema(type=protos.Type.STRING),
            ),
        ],
        [
            "list-list-int",
            list[list[int]],
            protos.Schema(
                type=protos.Type.ARRAY,
                items=protos.Schema(
                    protos.Schema(
                        type=protos.Type.ARRAY,
                        items=protos.Schema(type=protos.Type.INTEGER),
                    ),
                ),
            ),
        ],
        ["dict", dict, protos.Schema(type=protos.Type.OBJECT)],
        ["dict-str-any", dict[str, Any], protos.Schema(type=protos.Type.OBJECT)],
    )
    def test_auto_schema(self, annotation, expected):
        def fun(a: annotation):
            pass

        cfd = responder.FunctionDeclaration.from_function(fun)
        got = cfd.parameters.properties["a"]
        self.assertEqual(got, expected)


if __name__ == "__main__":
    absltest.main()
