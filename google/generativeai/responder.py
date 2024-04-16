from __future__ import annotations

from collections.abc import Iterable, Mapping, Sequence
import io
import inspect
import mimetypes
import typing
from typing import Any, Callable, Union
from typing_extensions import TypedDict

import pydantic

from google.generativeai.types import file_types
from google.ai import generativelanguage as glm


def _rename_schema_fields(schema):
    if schema is None:
        return schema

    schema = schema.copy()

    type_ = schema.pop("type", None)
    if type_ is not None:
        schema["type_"] = type_.upper()

    format_ = schema.pop("format", None)
    if format_ is not None:
        schema["format_"] = format_

    items = schema.pop("items", None)
    if items is not None:
        schema["items"] = _rename_schema_fields(items)

    properties = schema.pop("properties", None)
    if properties is not None:
        schema["properties"] = {k: _rename_schema_fields(v) for k, v in properties.items()}

    return schema


class FunctionDeclaration:
    def __init__(self, *, name: str, description: str, parameters: dict[str, Any] | None = None):
        """A  class wrapping a `glm.FunctionDeclaration`, describes a function for `genai.GenerativeModel`'s `tools`."""
        self._proto = glm.FunctionDeclaration(
            name=name, description=description, parameters=_rename_schema_fields(parameters)
        )

        @property
        def name(self) -> str:
            return self._proto.name

        @property
        def description(self) -> str:
            return self._proto.description

        @property
        def parameters(self) -> glm.Schema:
            return self._proto.parameters

        @classmethod
        def from_proto(cls, proto) -> FunctionDeclaration:
            self = cls(name="", description="", parameters={})
            self._proto = proto
            return self

        def to_proto(self) -> glm.FunctionDeclaration:
            return self._proto

    @staticmethod
    def from_function(function: Callable[..., Any], descriptions: dict[str, str] | None = None):
        """Builds a `CallableFunctionDeclaration` from a python function.

        The function should have type annotations.

        This method is able to generate the schema for arguments annotated with types:

        `AllowedTypes = float | int | str | list[AllowedTypes] | dict`

        This method does not yet build a schema for `TypedDict`, that would allow you to specify the dictionary
        contents. But you can build these manually.
        """

        if descriptions is None:
            descriptions = {}

        schema = _generate_schema(function, descriptions=descriptions)

        return CallableFunctionDeclaration(**schema, function=function)
    

StructType = dict[str, "ValueType"]
ValueType = Union[float, str, bool, StructType, list["ValueType"], None]

class CallableFunctionDeclaration(FunctionDeclaration):
    """An extension of `FunctionDeclaration` that can be built from a Python function, and is callable. 
    
    Note: The Python function must have type annotations.
    """

    def __init__(
            self,
            *,
            name: str,
            description: str,
            parameters: dict[str, Any] | None = None,
            function: Callable[..., Any],
    ):
        super().__init__(name=name, description=description, parameters=parameters)
        self.function = function

    def __call__(self, fc: glm.FunctionCall) -> glm.FunctionResponse:
        result = self.function(**fc.args)
        if not isinstance(result, dict):
            result = {"result": result}
        return glm.FunctionResponse(name=fc.name, response=result)   
    
FunctionDeclarationType = Union[
    FunctionDeclaration,
    glm.FunctionDeclaration,
    dict[str, Any],
    Callable[..., Any],
]

def _make_function_declaration(
    fun: FunctionDeclarationType,
) -> FunctionDeclaration | glm.FunctionDeclaration:
    if isinstance(fun, (FunctionDeclaration, glm.FunctionDeclaration)):
        return fun
    elif isinstance(fun, dict):
        if "function" in fun:
            return CallableFunctionDeclaration(**fun)
        else:
            return FunctionDeclaration(**fun)
    elif callable(fun):
        return CallableFunctionDeclaration.from_function(fun)
    else:
        raise TypeError(
            "Expected an instance of `genai.FunctionDeclaraionType`. Got a:\n" f"  {type(fun)=}\n",
            fun,
        )
    
def _encode_fd(fd: FunctionDeclaration | glm.FunctionDeclaration) -> glm.FunctionDeclaration:
    if isinstance(fd, glm.FunctionDeclaration):
        return fd

    return fd.to_proto()

class Tool:
    """A wrapper for `glm.Tool`, Contains a collection of related `FunctionDeclaration` objects."""

    def __init__(self, function_declarations: Iterable[FunctionDeclarationType]):
        # The main path doesn't use this but is seems useful.
        self._function_declarations = [_make_function_declaration(f) for f in function_declarations]
        self._index = {}
        for fd in self._function_declarations:
            name = fd.name
            if name in self._index:
                raise ValueError("")
            self._index[fd.name] = fd

        self._proto = glm.Tool(
            function_declarations=[_encode_fd(fd) for fd in self._function_declarations]
        )

    @property
    def function_declarations(self) -> list[FunctionDeclaration | glm.FunctionDeclaration]:
        return self._function_declarations

    def __getitem__(
        self, name: str | glm.FunctionCall
    ) -> FunctionDeclaration | glm.FunctionDeclaration:
        if not isinstance(name, str):
            name = name.name

        return self._index[name]

    def __call__(self, fc: glm.FunctionCall) -> glm.FunctionResponse | None:
        declaration = self[fc]
        if not callable(declaration):
            return None

        return declaration(fc)

    def to_proto(self):
        return self._proto
    
class ToolDict(TypedDict):
    function_declarations: list[FunctionDeclarationType]


ToolType = Union[
    Tool, glm.Tool, ToolDict, Iterable[FunctionDeclarationType], FunctionDeclarationType
]


def _make_tool(tool: ToolType) -> Tool:
    if isinstance(tool, Tool):
        return tool
    elif isinstance(tool, glm.Tool):
        return Tool(function_declarations=tool.function_declarations)
    elif isinstance(tool, dict):
        if "function_declarations" in tool:
            return Tool(**tool)
        else:
            fd = tool
            return Tool(function_declarations=[glm.FunctionDeclaration(**fd)])
    elif isinstance(tool, Iterable):
        return Tool(function_declarations=tool)
    else:
        try:
            return Tool(function_declarations=[tool])
        except Exception as e:
            raise TypeError(
                "Expected an instance of `genai.ToolType`. Got a:\n" f"  {type(tool)=}",
                tool,
            ) from e


class FunctionLibrary:
    """A container for a set of `Tool` objects, manages lookup and execution of their functions."""

    def __init__(self, tools: Iterable[ToolType]):
        tools = _make_tools(tools)
        self._tools = list(tools)
        self._index = {}
        for tool in self._tools:
            for declaration in tool.function_declarations:
                name = declaration.name
                if name in self._index:
                    raise ValueError(
                        f"A `FunctionDeclaration` named {name} is already defined. "
                        "Each `FunctionDeclaration` must be uniquely named."
                    )
                self._index[declaration.name] = declaration

    def __getitem__(
        self, name: str | glm.FunctionCall
    ) -> FunctionDeclaration | glm.FunctionDeclaration:
        if not isinstance(name, str):
            name = name.name

        return self._index[name]

    def __call__(self, fc: glm.FunctionCall) -> glm.Part | None:
        declaration = self[fc]
        if not callable(declaration):
            return None

        response = declaration(fc)
        return glm.Part(function_response=response)

    def to_proto(self):
        return [tool.to_proto() for tool in self._tools]


ToolsType = Union[Iterable[ToolType], ToolType]


def _make_tools(tools: ToolsType) -> list[Tool]:
    if isinstance(tools, Iterable) and not isinstance(tools, Mapping):
        tools = [_make_tool(t) for t in tools]
        if len(tools) > 1 and all(len(t.function_declarations) == 1 for t in tools):
            # flatten into a single tool.
            tools = [_make_tool([t.function_declarations[0] for t in tools])]
        return tools
    else:
        tool = tools
        return [_make_tool(tool)]


FunctionLibraryType = Union[FunctionLibrary, ToolsType]


def to_function_library(lib: FunctionLibraryType | None) -> FunctionLibrary | None:
    if lib is None:
        return lib
    elif isinstance(lib, FunctionLibrary):
        return lib
    else:
        return FunctionLibrary(tools=lib)


FunctionCallingMode = glm.FunctionCallingConfig.Mode

# fmt: off
_FUNCTION_CALLING_MODE = {
    1: FunctionCallingMode.AUTO,
    FunctionCallingMode.AUTO: FunctionCallingMode.AUTO,
    "mode_auto": FunctionCallingMode.AUTO,
    "auto": FunctionCallingMode.AUTO,

    2: FunctionCallingMode.ANY,
    FunctionCallingMode.ANY: FunctionCallingMode.ANY,
    "mode_any": FunctionCallingMode.ANY,
    "any": FunctionCallingMode.ANY,

    3: FunctionCallingMode.NONE,
    FunctionCallingMode.NONE: FunctionCallingMode.NONE,
    "mode_none": FunctionCallingMode.NONE,
    "none": FunctionCallingMode.NONE,
}
# fmt: on

FunctionCallingModeType = Union[FunctionCallingMode, str, int]


def to_function_calling_mode(x: FunctionCallingModeType) -> FunctionCallingMode:
    if isinstance(x, str):
        x = x.lower()
    return _FUNCTION_CALLING_MODE[x]


class FunctionCallingConfigDict(TypedDict):
    mode: FunctionCallingModeType
    allowed_function_names: list[str]


FunctionCallingConfigType = Union[
    FunctionCallingModeType, FunctionCallingConfigDict, glm.FunctionCallingConfig
]


def to_function_calling_config(obj: FunctionCallingConfigType) -> glm.FunctionCallingConfig:
    if isinstance(obj, glm.FunctionCallingConfig):
        return obj
    elif isinstance(obj, (FunctionCallingMode, str, int)):
        obj = {"mode": to_function_calling_mode(obj)}
    elif isinstance(obj, dict):
        obj = obj.copy()
        mode = obj.pop("mode")
        obj["mode"] = to_function_calling_mode(mode)
    else:
        raise TypeError(
            f"Could not convert input to `glm.FunctionCallingConfig`: \n'" f"  type: {type(obj)}\n",
            obj,
        )

    return glm.FunctionCallingConfig(obj)


class ToolConfigDict:
    function_calling_config: FunctionCallingConfigType


ToolConfigType = Union[ToolConfigDict, glm.ToolConfig]


def to_tool_config(obj: ToolConfigType) -> glm.ToolConfig:
    if isinstance(obj, glm.ToolConfig):
        return obj
    elif isinstance(obj, dict):
        fcc = obj.pop("function_calling_config")
        fcc = to_function_calling_config(fcc)
        obj["function_calling_config"] = fcc
        return glm.ToolConfig(**obj)
    else:
        raise TypeError(
            f"Could not convert input to `glm.ToolConfig`: \n'" f"  type: {type(obj)}\n", obj
        )