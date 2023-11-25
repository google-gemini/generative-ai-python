import copy
import pathlib
import unittest.mock

from absl.testing import absltest
from absl.testing import parameterized
import google.ai.generativelanguage as glm
import google.generativeai as genai
from google.generativeai.types import content_types
from google.generativeai.types import safety_types
import IPython.display
import PIL.Image


HERE = pathlib.Path(__file__).parent
TEST_IMAGE_PATH = HERE / "test_img.png"
TEST_IMAGE_URL = "https://storage.googleapis.com/generativeai-downloads/data/test_img.png"
TEST_IMAGE_DATA = TEST_IMAGE_PATH.read_bytes()


class UnitTests(parameterized.TestCase):
    @parameterized.named_parameters(
        ["PIL", PIL.Image.open(TEST_IMAGE_PATH)],
        ["IPython", IPython.display.Image(filename=TEST_IMAGE_PATH)],
    )
    def test_image_to_blob(self, image):
        blob = content_types.image_to_blob(image)
        self.assertIsInstance(blob, glm.Blob)
        self.assertEqual(blob.mime_type, "image/png")
        self.assertStartsWith(blob.data, b"\x89PNG")

    @parameterized.named_parameters(
        ["BlobDict", {"mime_type": "image/png", "data": TEST_IMAGE_DATA}],
        ["glm.Blob", glm.Blob(mime_type="image/png", data=TEST_IMAGE_DATA)],
        ["Image", IPython.display.Image(filename=TEST_IMAGE_PATH)],
    )
    def test_to_blob(self, example):
        blob = content_types.to_blob(example)
        self.assertIsInstance(blob, glm.Blob)
        self.assertEqual(blob.mime_type, "image/png")
        self.assertStartsWith(blob.data, b"\x89PNG")

    @parameterized.named_parameters(
        ["dict", {"text": "Hello world!"}],
        ["glm.Part", glm.Part(text="Hello world!")],
        ["str", "Hello world!"],
    )
    def test_to_part(self, example):
        part = content_types.to_part(example)
        self.assertIsInstance(part, glm.Part)
        self.assertEqual(part.text, "Hello world!")

    @parameterized.named_parameters(
        ["Image", IPython.display.Image(filename=TEST_IMAGE_PATH)],
        ["BlobDict", {"mime_type": "image/png", "data": TEST_IMAGE_DATA}],
        [
            "PartDict",
            {"inline_data": {"mime_type": "image/png", "data": TEST_IMAGE_DATA}},
        ],
    )
    def test_img_to_part(self, example):
        blob = content_types.to_part(example).inline_data
        self.assertIsInstance(blob, glm.Blob)
        self.assertEqual(blob.mime_type, "image/png")
        self.assertStartsWith(blob.data, b"\x89PNG")

    @parameterized.named_parameters(
        ["glm.Content", glm.Content(parts=[{"text": "Hello world!"}])],
        ["ContentDict", {"parts": [{"text": "Hello world!"}]}],
        ["ContentDict-str", {"parts": ["Hello world!"]}],
        ["list[parts]", [{"text": "Hello world!"}]],
        ["list[str]", ["Hello world!"]],
        ["iterator[parts]", iter([{"text": "Hello world!"}])],
        ["part", {"text": "Hello world!"}],
        ["str", "Hello world!"],
    )
    def test_to_content(self, example):
        content = content_types.to_content(example)
        part = content.parts[0]

        self.assertLen(content.parts, 1)
        self.assertIsInstance(part, glm.Part)
        self.assertEqual(part.text, "Hello world!")

    @parameterized.named_parameters(
        ["ContentDict", {"parts": [PIL.Image.open(TEST_IMAGE_PATH)]}],
        ["list[Image]", [PIL.Image.open(TEST_IMAGE_PATH)]],
        ["Image", PIL.Image.open(TEST_IMAGE_PATH)],
    )
    def test_img_to_content(self, example):
        content = content_types.to_content(example)
        blob = content.parts[0].inline_data
        self.assertLen(content.parts, 1)
        self.assertIsInstance(blob, glm.Blob)
        self.assertEqual(blob.mime_type, "image/png")
        self.assertStartsWith(blob.data, b"\x89PNG")

    @parameterized.named_parameters(
        ["glm.Content", glm.Content(parts=[{"text": "Hello world!"}])],
        ["ContentDict", {"parts": [{"text": "Hello world!"}]}],
        ["ContentDict-str", {"parts": ["Hello world!"]}],
    )
    def test_strict_to_content(self, example):
        content = content_types.strict_to_content(example)
        part = content.parts[0]

        self.assertLen(content.parts, 1)
        self.assertIsInstance(part, glm.Part)
        self.assertEqual(part.text, "Hello world!")

    @parameterized.named_parameters(
        ["list[parts]", [{"text": "Hello world!"}]],
        ["list[str]", ["Hello world!"]],
        ["iterator[parts]", iter([{"text": "Hello world!"}])],
        ["part", {"text": "Hello world!"}],
        ["str", "Hello world!"],
    )
    def test_strict_to_contents_fails(self, examples):
        with self.assertRaises(TypeError):
            content_types.strict_to_content(examples)

    @parameterized.named_parameters(
        ["glm.Content", [glm.Content(parts=[{"text": "Hello world!"}])]],
        ["ContentDict", [{"parts": [{"text": "Hello world!"}]}]],
        ["ContentDict-unwraped", [{"parts": ["Hello world!"]}]],
    )
    def test_to_contents(self, example):
        contents = content_types.to_contents(example)
        part = contents[0].parts[0]

        self.assertLen(contents, 1)
        self.assertLen(contents[0].parts, 1)
        self.assertIsInstance(part, glm.Part)
        self.assertEqual(part.text, "Hello world!")

    def test_dict_to_content_fails(self):
        with self.assertRaises(KeyError):
            content_types.to_content({"bad": "dict"})

    @parameterized.named_parameters(
        [
            "ContentDict",
            [{"parts": [{"inline_data": PIL.Image.open(TEST_IMAGE_PATH)}]}],
        ],
        ["ContentDict-unwraped", [{"parts": [PIL.Image.open(TEST_IMAGE_PATH)]}]],
        ["Image", PIL.Image.open(TEST_IMAGE_PATH)],
    )
    def test_img_to_contents(self, example):
        contents = content_types.to_contents(example)
        blob = contents[0].parts[0].inline_data

        self.assertLen(contents, 1)
        self.assertLen(contents[0].parts, 1)
        self.assertIsInstance(blob, glm.Blob)
        self.assertEqual(blob.mime_type, "image/png")
        self.assertStartsWith(blob.data, b"\x89PNG")


if __name__ == "__main__":
    absltest.main()
