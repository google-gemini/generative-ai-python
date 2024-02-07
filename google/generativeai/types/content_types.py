from __future__ import annotations

from collections.abc import Iterable, Mapping
import io
import inspect
import mimetypes
import typing
from typing import Any, Callable, Mapping, Sequence, TypedDict, Union

import pydantic

from google.ai import generativelanguage as glm

if typing.TYPE_CHECKING:
    import PIL.Image
    import IPython.display

    IMAGE_TYPES = (PIL.Image.Image, IPython.display.Image)
else:
    IMAGE_TYPES = ()
    try:
        import PIL.Image

        IMAGE_TYPES = IMAGE_TYPES + (PIL.Image.Image,)
    except ImportError:
        PIL = None

    try:
        import IPython.display

        IMAGE_TYPES = IMAGE_TYPES + (IPython.display.Image,)
    except ImportError:
        IPython = None


__all__ = [
    "BlobDict",
    "BlobType",
    "PartDict",
    "PartType",
    "ContentDict",
    "ContentType",
    "StrictContentType",
    "ContentsType",
    "ToolsType",
]


def pil_to_blob(img):
    bytesio = io.BytesIO()
    if isinstance(img, PIL.PngImagePlugin.PngImageFile):
        img.save(bytesio, format="PNG")
        mime_type = "image/png"
    else:
        img.save(bytesio, format="JPEG")
        mime_type = "image/jpeg"
    bytesio.seek(0)
    data = bytesio.read()
    return glm.Blob(mime_type=mime_type, data=data)


def image_to_blob(image) -> glm.Blob:
    if PIL is not None:
        if isinstance(image, PIL.Image.Image):
            return pil_to_blob(image)

    if IPython is not None:
        if isinstance(image, IPython.display.Image):
            name = image.filename
            if name is None:
                raise ValueError(
                    "Can only convert `IPython.display.Image` if "
                    "it is constructed from a local file (Image(filename=...))."
                )

            mime_type, _ = mimetypes.guess_type(name)
            if mime_type is None:
                mime_type = "image/unknown"

            return glm.Blob(mime_type=mime_type, data=image.data)

    raise TypeError(
        "Could not convert image. expected an `Image` type"
        "(`PIL.Image.Image` or `IPython.display.Image`).\n"
        f"Got a: {type(image)}\n"
        f"Value: {image}"
    )


class BlobDict(TypedDict):
    mime_type: str
    data: bytes


def _convert_dict(d: Mapping) -> glm.Content | glm.Part | glm.Blob:
    if is_content_dict(d):
        content = dict(d)
        content["parts"] = [to_part(part) for part in content["parts"]]
        return glm.Content(content)
    elif is_part_dict(d):
        part = dict(d)
        if "inline_data" in part:
            part["inline_data"] = to_blob(part["inline_data"])
        return glm.Part(part)
    elif is_blob_dict(d):
        blob = d
        return glm.Blob(blob)
    else:
        raise KeyError(
            "Could not recognize the intended type of the `dict`. "
            "A `Content` should have a 'parts' key. "
            "A `Part` should have a 'inline_data' or a 'text' key. "
            "A `Blob` should have 'mime_type' and 'data' keys. "
            f"Got keys: {list(d.keys())}"
        )


def is_blob_dict(d):
    return "mime_type" in d and "data" in d


if typing.TYPE_CHECKING:
    BlobType = Union[
        glm.Blob, BlobDict, PIL.Image.Image, IPython.display.Image
    ]  # Any for the images
else:
    BlobType = Union[glm.Blob, BlobDict, Any]


def to_blob(blob: BlobType) -> glm.Blob:
    if isinstance(blob, Mapping):
        blob = _convert_dict(blob)

    if isinstance(blob, glm.Blob):
        return blob
    elif isinstance(blob, IMAGE_TYPES):
        return image_to_blob(blob)
    else:
        if isinstance(blob, Mapping):
            raise KeyError(
                "Could not recognize the intended type of the `dict`\n" "A content should have "
            )
        raise TypeError(
            "Could not create `Blob`, expected `Blob`, `dict` or an `Image` type"
            "(`PIL.Image.Image` or `IPython.display.Image`).\n"
            f"Got a: {type(blob)}\n"
            f"Value: {blob}"
        )


class PartDict(TypedDict):
    text: str
    inline_data: BlobType


# When you need a `Part` accept a part object, part-dict, blob or string
PartType = Union[glm.Part, PartDict, BlobType, str]


def is_part_dict(d):
    return "text" in d or "inline_data" in d


def to_part(part: PartType):
    if isinstance(part, Mapping):
        part = _convert_dict(part)

    if isinstance(part, glm.Part):
        return part
    elif isinstance(part, str):
        return glm.Part(text=part)
    else:
        # Maybe it can be turned into a blob?
        return glm.Part(inline_data=to_blob(part))


class ContentDict(TypedDict):
    parts: list[PartType]
    role: str


def is_content_dict(d):
    return "parts" in d


# When you need a message accept a `Content` object or dict, a list of parts,
# or a single part
ContentType = Union[glm.Content, ContentDict, Iterable[PartType], PartType]

# For generate_content, we're not guessing roles for [[parts],[parts],[parts]] yet.
StrictContentType = Union[glm.Content, ContentDict]


def to_content(content: ContentType):
    if not content:
        raise ValueError("content must not be empty")

    if isinstance(content, Mapping):
        content = _convert_dict(content)

    if isinstance(content, glm.Content):
        return content
    elif isinstance(content, Iterable) and not isinstance(content, str):
        return glm.Content(parts=[to_part(part) for part in content])
    else:
        # Maybe this is a Part?
        return glm.Content(parts=[to_part(content)])


def strict_to_content(content: StrictContentType):
    if isinstance(content, Mapping):
        content = _convert_dict(content)

    if isinstance(content, glm.Content):
        return content
    else:
        raise TypeError(
            "Expected a `glm.Content` or a `dict(parts=...)`.\n"
            f"Got type: {type(content)}\n"
            f"Value: {content}\n"
        )


ContentsType = Union[ContentType, Iterable[StrictContentType], None]


def to_contents(contents: ContentsType) -> list[glm.Content]:
    if contents is None:
        return []

    if isinstance(contents, Iterable) and not isinstance(contents, (str, Mapping)):
        try:
            # strict_to_content so [[parts], [parts]] doesn't assume roles.
            contents = [strict_to_content(c) for c in contents]
            return contents
        except TypeError:
            # If you get a TypeError here it's probably because that was a list
            # of parts, not a list of contents, so fall back to `to_content`.
            pass

    contents = [to_content(contents)]
    return contents

def generate_schema(
        f: Callable[..., Any],
        *,
        descriptions: Mapping[str, str] = {},
        required: Sequence[str] = [],
    ) -> dict[str:Any]:
    """Generates the OpenAPI Schema for a python function.

    Args:
        f (Callable):
            Required. The function to generate an OpenAPI Schema for.
        descriptions (Mapping[str, str]):
            Optional. A `{name: description}` mapping for annotating input
            arguments of the function with user-provided descriptions. It
            defaults to an empty dictionary (i.e. there will not be any
            description for any of the inputs).
        required (Sequence[str]):
            Optional. For the user to specify the set of required arguments in
            function calls to `f`. If specified, it will be automatically
            inferred from `f`.

    Returns:
        dict[str, Any]: The OpenAPI Schema for the function `f` in JSON format.
    """
    defaults = dict(inspect.signature(f).parameters)
    fields_dict = {
        name: (
            # 1. We infer the argument type here: use Any rather than None so
            # it will not try to auto-infer the type based on the default value.
            (
                param.annotation if param.annotation != inspect.Parameter.empty
                else Any
            ),
            pydantic.Field(
                # 2. We do not support default values for now.
                # default=(
                #     param.default if param.default != inspect.Parameter.empty
                #     else None
                # ),
                # 3. We support user-provided descriptions.
                description=descriptions.get(name, None),
            )
        )
        for name, param in defaults.items()
        # We do not support *args or **kwargs
        if param.kind in (
            inspect.Parameter.POSITIONAL_OR_KEYWORD,
            inspect.Parameter.KEYWORD_ONLY,
            inspect.Parameter.POSITIONAL_ONLY,
        )
    }
    parameters = pydantic.create_model(f.__name__, **fields_dict).schema()
    # Postprocessing
    # 4. Suppress unnecessary title generation:
    #    * https://github.com/pydantic/pydantic/issues/1051
    #    * http://cl/586221780
    parameters.pop('title')
    for name, function_arg in parameters.get("properties", {}).items():
        function_arg.pop("title")
        annotation = defaults[name].annotation
        # 5. Nullable fields:
        #     * https://github.com/pydantic/pydantic/issues/1270
        #     * https://stackoverflow.com/a/58841311
        #     * https://github.com/pydantic/pydantic/discussions/4872
        if (
                typing.get_origin(annotation) is typing.Union
                and type(None) in typing.get_args(annotation)
            ):
            function_arg["nullable"] = True
    # 6. Annotate required fields.
    if required:
        # We use the user-provided "required" fields if specified.
        parameters["required"] = required
    else:
        # Otherwise we infer it from the function signature.
        parameters["required"] = [
            k for k in defaults if (
                defaults[k].default == inspect.Parameter.empty
                and defaults[k].kind in (
                    inspect.Parameter.POSITIONAL_OR_KEYWORD,
                    inspect.Parameter.KEYWORD_ONLY,
                    inspect.Parameter.POSITIONAL_ONLY,
                )
            )
        ]
    schema = dict(name=f.__name__, description=f.__doc__, parameters=parameters)
    return schema




ToolsType = Union[
    Iterable[glm.Tool],
    glm.Tool,
    dict[str, Any],
    None]


def _rename_schema_fields(schema):
  schema = schema.copy()

  type_ = schema.pop('type', None)
  if type_ is not None:
    schema['type_'] = type_.upper()

  format_ = schema.pop('format', None)
  if format_ is not None:
    schema['format_'] = format_

  items = schema.pop('items', None)
  if items is not None:
    schema['items'] = rename_schema_fields(items)

  properties = schema.pop('properties', None)
  if properties is not None:
    schema['properties'] = {k: rename_schema_fields(v) for k,v in properties.items()}

  return schema


@dataclasses.dataclass
class FunctionDeclaration:
  name:str
  description:str
  parameters:Any

  def _encode(self):
    p = rename_schema_fields(self.parameters)

    return glm.FunctionDeclaration(
        name=self.name,
        description=self.description,
        parameters=p
    )

@dataclasses.dataclass
class CallableFunctionDeclaration(FunctionDeclaration):
  function: Callable[..., Any]

  @classmethod
  def from_function(cls, f, descriptions:dict[str, Any]|None=None):
    if descriptions is None:
      descriptions={}

    schema = generate_schema.generate_schema(f, descriptions=descriptions)

    return cls(
        **schema,
        function = f)

  def __call__(self, fc: glm.FunctionCall) -> glm.FunctionResponse:
    args = {}


@dataclasses.dataclass
class Tool:
  functions: list[FunctionDeclaration]

  def __init__(self, functions):
    # The main path doesn't use this but is seems useful.
    self.functions = list(functions)
    self._index = {}
    for fd in self.functions:
      name = fd.name
      if name in self._index:
          raise ValueError('')
      self._index[fd.name] = fd

  def __call__(self, fc: glm.FunctionCall) -> glm.FunctionResponse:
    name = fc.name
    declaration = self._index[name]
    if not callable(declaration):
      return None

    return declaration(fc)


@dataclasses.dataclass(init=False)
class FunctionLibrary:
  tools: list[Tool]

  def __init__(self, tools):
    self.tools = list(tools)
    self._index = {}
    for tool in self.tools:
      for declaration in tool:
        name = declaration.name
        if name in self._index:
            raise ValueError('')
        self._index[declaration.name] = declaration

  def __call__(self, fc: glm.FunctionCall) -> glm.Content | None:
    name = fc.name
    declaration = self._index[name]
    if not callable(declaration):
      return None

    response = declaration(fc)
    return glm.Content(
        role='user',
        parts=[response]
    )

def to_tools(tools: ToolsType) -> list[glm.Tool]:
    if tools is None:
        return []
    elif isinstance(tools, Mapping):
        return [glm.Tool(tools)]
    elif isinstance(tools, Iterable):
        return [glm.Tool(t) for t in tools]
    else:
        return [glm.Tool(tools)]
