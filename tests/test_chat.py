import collections
from collections.abc import Iterable
import copy
import pathlib
from typing import Any
import textwrap
import unittest.mock
from absl.testing import absltest
from absl.testing import parameterized
from google.generativeai import protos
from google.generativeai import client as client_lib
from google.generativeai import generative_models
from google.generativeai.types import content_types
from google.generativeai.types import generation_types
from google.generativeai.types import helper_types


import PIL.Image

HERE = pathlib.Path(__file__).parent
TEST_IMAGE_PATH = HERE / "test_img.png"
TEST_IMAGE_URL = "https://storage.googleapis.com/generativeai-downloads/data/test_img.png"
TEST_IMAGE_DATA = TEST_IMAGE_PATH.read_bytes()


def simple_part(text: str) -> protos.Content:
    return protos.Content({"parts": [{"text": text}]})


def noop(x: int):
    return x


def iter_part(texts: Iterable[str]) -> protos.Content:
    return protos.Content({"parts": [{"text": t} for t in texts]})


def simple_response(text: str) -> protos.GenerateContentResponse:
    return protos.GenerateContentResponse({"candidates": [{"content": simple_part(text)}]})


class MockGenerativeServiceClient:
    def __init__(self, test):
        self.test = test
        self.observed_requests = []
        self.observed_kwargs = []
        self.responses = collections.defaultdict(list)

    def generate_content(
        self,
        request: protos.GenerateContentRequest,
        **kwargs,
    ) -> protos.GenerateContentResponse:
        self.test.assertIsInstance(request, protos.GenerateContentRequest)
        self.observed_requests.append(request)
        self.observed_kwargs.append(kwargs)
        response = self.responses["generate_content"].pop(0)
        return response

    def stream_generate_content(
        self,
        request: protos.GetModelRequest,
        **kwargs,
    ) -> Iterable[protos.GenerateContentResponse]:
        self.observed_requests.append(request)
        self.observed_kwargs.append(kwargs)
        response = self.responses["stream_generate_content"].pop(0)
        return response

    def count_tokens(
        self,
        request: protos.CountTokensRequest,
        **kwargs,
    ) -> Iterable[protos.GenerateContentResponse]:
        self.observed_requests.append(request)
        self.observed_kwargs.append(kwargs)
        response = self.responses["count_tokens"].pop(0)
        return response


class CUJTests(parameterized.TestCase):
    """Tests are in order with the design doc."""

    @property
    def observed_requests(self):
        return self.client.observed_requests

    @property
    def observed_kwargs(self):
        return self.client.observed_kwargs

    @property
    def responses(self):
        return self.client.responses

    def setUp(self):
        self.client = MockGenerativeServiceClient(self)
        client_lib._client_manager.clients["generative"] = self.client

    def test_chat(self):
        # Multi turn chat
        model = generative_models.GenerativeModel("gemini-pro")
        chat = model.start_chat()

        self.responses["generate_content"] = [
            simple_response("first"),
            simple_response("second"),
            simple_response("third"),
        ]

        msg1 = "I really like fantasy books."
        response = chat.send_message(msg1)
        self.assertEqual(response.text, "first")
        self.assertEqual(self.observed_requests[0].contents[0].parts[0].text, msg1)

        msg2 = "I also like this image."
        response = chat.send_message([msg2, PIL.Image.open(TEST_IMAGE_PATH)])

        self.assertEqual(response.text, "second")
        self.assertEqual(self.observed_requests[1].contents[0].parts[0].text, msg1)
        self.assertEqual(self.observed_requests[1].contents[1].parts[0].text, "first")
        self.assertEqual(self.observed_requests[1].contents[2].parts[0].text, msg2)
        self.assertEqual(
            self.observed_requests[1].contents[2].parts[1].inline_data.data[:4],
            b"\x89PNG",
        )

        msg3 = "What things do I like?."
        response = chat.send_message(msg3)
        self.assertEqual(response.text, "third")
        self.assertLen(chat.history, 6)

    def test_chat_roles(self):
        self.responses["generate_content"] = [simple_response("hello!")]

        model = generative_models.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        response = chat.send_message("hello?")
        history = chat.history
        self.assertEqual(history[0].role, "user")
        self.assertEqual(history[1].role, "model")

    def test_chat_streaming_basic(self):
        # Chat streaming
        self.responses["stream_generate_content"] = [
            iter([simple_response("a"), simple_response("b"), simple_response("c")]),
            iter([simple_response("1"), simple_response("2"), simple_response("3")]),
            iter([simple_response("x"), simple_response("y"), simple_response("z")]),
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat()

        response = chat.send_message("letters?", stream=True)

        self.assertEqual("".join(chunk.text for chunk in response), "abc")

        response = chat.send_message("numbers?", stream=True)

        self.assertEqual("".join(chunk.text for chunk in response), "123")

        response = chat.send_message("more letters?", stream=True)

        self.assertEqual("".join(chunk.text for chunk in response), "xyz")

    def test_chat_incomplete_streaming_errors(self):
        # Chat streaming
        self.responses["stream_generate_content"] = [
            iter([simple_response("a"), simple_response("b"), simple_response("c")]),
            iter([simple_response("1"), simple_response("2"), simple_response("3")]),
            iter([simple_response("x"), simple_response("y"), simple_response("z")]),
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat()
        response = chat.send_message("letters?", stream=True)

        with self.assertRaises(generation_types.IncompleteIterationError):
            chat.history

        with self.assertRaises(generation_types.IncompleteIterationError):
            chat.send_message("numbers?", stream=True)

        for chunk in response:
            pass
        self.assertLen(chat.history, 2)

        response = chat.send_message("numbers?", stream=True)
        self.assertEqual("".join(chunk.text for chunk in response), "123")

    def test_edit_history(self):
        self.responses["generate_content"] = [
            simple_response("first"),
            simple_response("second"),
            simple_response("third"),
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat()

        response = chat.send_message("hello")
        self.assertEqual(response.text, "first")
        self.assertLen(chat.history, 2)

        response = chat.send_message("hello")
        self.assertEqual(response.text, "second")
        self.assertLen(chat.history, 4)

        chat.history[-1] = content_types.to_content("edited")
        response = chat.send_message("hello")
        self.assertEqual(response.text, "third")
        self.assertLen(chat.history, 6)

        self.assertEqual(chat.history[3], content_types.to_content("edited"))
        self.assertEqual(self.observed_requests[-1].contents[3].parts[0].text, "edited")

    def test_replace_history(self):
        self.responses["generate_content"] = [
            simple_response("first"),
            simple_response("second"),
            simple_response("third"),
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat()
        chat.send_message("hello1")
        chat.send_message("hello2")

        self.assertLen(chat.history, 4)
        chat.history = [{"parts": ["Goodbye"]}, {"parts": ["Later gater"]}]
        self.assertLen(chat.history, 2)

        response = chat.send_message("hello3")
        self.assertEqual(response.text, "third")
        self.assertLen(chat.history, 4)

        self.assertEqual(self.observed_requests[-1].contents[0].parts[0].text, "Goodbye")

    def test_copy_history(self):
        self.responses["generate_content"] = [
            simple_response("first"),
            simple_response("second"),
            simple_response("third"),
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat1 = model.start_chat()
        chat1.send_message("hello1")

        chat2 = copy.copy(chat1)
        chat2.send_message("hello2")

        chat1.send_message("hello3")

        self.assertLen(chat1.history, 4)
        expected = [
            {"role": "user", "parts": ["hello1"]},
            {"role": "model", "parts": ["first"]},
            {"role": "user", "parts": ["hello3"]},
            {"role": "model", "parts": ["third"]},
        ]
        for content, ex in zip(chat1.history, expected):
            self.assertEqual(content, content_types.to_content(ex))

        self.assertLen(chat2.history, 4)
        expected = [
            {"role": "user", "parts": ["hello1"]},
            {"role": "model", "parts": ["first"]},
            {"role": "user", "parts": ["hello2"]},
            {"role": "model", "parts": ["second"]},
        ]
        for content, ex in zip(chat2.history, expected):
            self.assertEqual(content, content_types.to_content(ex))

    def test_chat_error_in_stream(self):
        def throw():
            for c in "123":
                yield simple_response(c)
            raise ValueError()

        def no_throw():
            for c in "abc":
                yield simple_response(c)

        self.responses["stream_generate_content"] = [
            no_throw(),
            throw(),
            no_throw(),
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat()

        # Send a message, the response is okay..
        chat.send_message("hello1", stream=True).resolve()

        # Send a second message, it fails
        response = chat.send_message("hello2", stream=True)
        with self.assertRaises(ValueError):
            # Iteration fails
            for chunk in response:
                pass

        # Since the response broke, we can't access the history
        with self.assertRaises(generation_types.BrokenResponseError):
            chat.history

        # or send another message.
        with self.assertRaises(generation_types.BrokenResponseError):
            chat.send_message("hello")

        # Rewind a step to before the error
        chat.rewind()

        self.assertLen(chat.history, 2)
        self.assertEqual(chat.history[0].parts[0].text, "hello1")
        self.assertEqual(chat.history[1].parts[0].text, "abc")

        # And continue
        chat.send_message("hello3", stream=True).resolve()
        self.assertLen(chat.history, 4)
        self.assertEqual(chat.history[2].parts[0].text, "hello3")
        self.assertEqual(chat.history[3].parts[0].text, "abc")

    def test_chat_prompt_blocked(self):
        self.responses["generate_content"] = [
            protos.GenerateContentResponse(
                {
                    "prompt_feedback": {"block_reason": "SAFETY"},
                }
            )
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat()

        with self.assertRaises(generation_types.BlockedPromptException):
            chat.send_message("hello")

        self.assertLen(chat.history, 0)

    def test_chat_candidate_blocked(self):
        # I feel like chat needs a .last so you can look at the partial results.
        self.responses["generate_content"] = [
            protos.GenerateContentResponse(
                {
                    "candidates": [{"finish_reason": "SAFETY"}],
                }
            )
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat()

        with self.assertRaises(generation_types.StopCandidateException):
            chat.send_message("hello")

    def test_chat_streaming_unexpected_stop(self):
        self.responses["stream_generate_content"] = [
            iter(
                [
                    simple_response("a"),
                    simple_response("b"),
                    simple_response("c"),
                    protos.GenerateContentResponse(
                        {
                            "candidates": [{"finish_reason": "SAFETY"}],
                        }
                    ),
                ]
            )
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat()

        response = chat.send_message("hello", stream=True)
        for chunk in response:
            # The result doesn't know it's a chat result so it can't throw.
            # Unless we give it some way to know?
            pass

        with self.assertRaises(generation_types.BrokenResponseError):
            # But when preparing the next message, we can throw:
            response = chat.send_message("hello2", stream=True)

        # It's a little bad that here it's only on send message that you find out
        # about the problem. "hello2" is never added, the `rewind` removes `hello1`.
        chat.rewind()
        self.assertLen(chat.history, 0)

    def test_tools(self):
        tools = dict(
            function_declarations=[
                dict(name="datetime", description="Returns the current UTC date and time.")
            ]
        )
        model = generative_models.GenerativeModel("gemini-pro-vision", tools=tools)

        self.responses["generate_content"] = [
            simple_response("a"),
            simple_response("b"),
        ]

        response = model.generate_content("Hello")

        chat = model.start_chat()
        response = chat.send_message("Hello")

        expect_tools = dict(
            function_declarations=[
                dict(name="datetime", description="Returns the current UTC date and time.")
            ]
        )

        for obr in self.observed_requests:
            self.assertLen(obr.tools, 1)
            self.assertEqual(type(obr.tools[0]).to_dict(obr.tools[0]), tools)

    @parameterized.named_parameters(
        [
            "ChatSession.send_message",
            generative_models.ChatSession.send_message,
            generative_models.ChatSession.send_message_async,
        ],
        [
            "ChatSession._handle_afc",
            generative_models.ChatSession._handle_afc,
            generative_models.ChatSession._handle_afc_async,
        ],
    )
    def test_async_code_match(self, obj, aobj):
        import inspect
        import re

        source = inspect.getsource(obj)
        asource = inspect.getsource(aobj)

        source = re.sub('""".*"""', "", source, flags=re.DOTALL)
        asource = re.sub('""".*"""', "", asource, flags=re.DOTALL)

        asource = (
            asource.replace("anext", "next")
            .replace("aiter", "iter")
            .replace("_async", "")
            .replace("async ", "")
            .replace("await ", "")
            .replace("Async", "")
            .replace("ASYNC_", "")
        )

        asource = re.sub(" *?# type: ignore", "", asource)
        self.assertEqual(source, asource, f"error in {obj=}")

    def test_repr_error_info_for_chat_error_in_stream(self):
        # response._error => ValueError
        def throw():
            for c in "123":
                yield simple_response(c)
            raise ValueError()

        def no_throw():
            for c in "abc":
                yield simple_response(c)

        self.responses["stream_generate_content"] = [
            no_throw(),
            throw(),
            no_throw(),
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat()

        # Send a message, the response is okay..
        chat.send_message("hello1", stream=True).resolve()

        # Send a second message, it fails
        response = chat.send_message("hello2", stream=True)
        with self.assertRaises(ValueError):
            # Iteration fails
            for chunk in response:
                pass

        result = repr(response)
        expected = textwrap.dedent(
            """\
            response:
            GenerateContentResponse(
                done=True,
                iterator=None,
                result=protos.GenerateContentResponse({
                  "candidates": [
                    {
                      "content": {
                        "parts": [
                          {
                            "text": "123"
                          }
                        ]
                      },
                      "index": 0,
                      "citation_metadata": {}
                    }
                  ],
                  "prompt_feedback": {},
                  "usage_metadata": {}
                }),
            ),
            error=<ValueError> """
        )
        self.assertEqual(expected, result)

    def test_repr_error_info_for_chat_streaming_unexpected_stop(self):
        # response._error => StopCandidateException
        self.responses["stream_generate_content"] = [
            iter(
                [
                    simple_response("a"),
                    simple_response("b"),
                    simple_response("c"),
                    protos.GenerateContentResponse(
                        {
                            "candidates": [{"finish_reason": "SAFETY"}],
                        }
                    ),
                ]
            )
        ]

        model = generative_models.GenerativeModel("gemini-pro-vision")
        chat = model.start_chat()

        response = chat.send_message("hello", stream=True)
        for chunk in response:
            # The result doesn't know it's a chat result so it can't throw.
            # Unless we give it some way to know?
            pass

        with self.assertRaises(generation_types.BrokenResponseError):
            # But when preparing the next message, we can throw:
            response = chat.send_message("hello2", stream=True)

        result = repr(response)
        expected = textwrap.dedent(
            """\
            response:
            GenerateContentResponse(
                done=True,
                iterator=None,
                result=protos.GenerateContentResponse({
                  "candidates": [
                    {
                      "content": {
                        "parts": [
                          {
                            "text": "abc"
                          }
                        ]
                      },
                      "finish_reason": "SAFETY",
                      "index": 0,
                      "citation_metadata": {}
                    }
                  ],
                  "prompt_feedback": {},
                  "usage_metadata": {}
                }),
            ),
            error=<StopCandidateException> index: 0
            content {
              parts {
                text: "abc"
              }
            }
            finish_reason: SAFETY
            citation_metadata {
            }
            """
        )
        self.assertEqual(expected, result)

    def test_repr_for_multi_turn_chat(self):
        # Multi turn chat
        model = generative_models.GenerativeModel("gemini-pro")
        chat = model.start_chat()

        self.responses["generate_content"] = [
            simple_response("first"),
            simple_response("second"),
            simple_response("third"),
        ]

        msg1 = "I really like fantasy books."
        response = chat.send_message(msg1)

        msg2 = "I also like this image."
        response = chat.send_message([msg2, PIL.Image.open(TEST_IMAGE_PATH)])

        msg3 = "What things do I like?."
        response = chat.send_message(msg3)

        result = repr(chat)
        expected = textwrap.dedent(
            """\
            ChatSession(
                model=genai.GenerativeModel(
                    model_name='models/gemini-pro',
                    generation_config={},
                    safety_settings={},
                    tools=None,
                    system_instruction=None,
                ),
                history=[protos.Content({'parts': [{'text': 'I really like fantasy books.'}], 'role': 'user'}), protos.Content({'parts': [{'text': 'first'}], 'role': 'model'}), protos.Content({'parts': [{'text': 'I also like this image.'}, {'inline_data': {'data': 'iVBORw0KGgoA...AAElFTkSuQmCC', 'mime_type': 'image/png'}}], 'role': 'user'}), protos.Content({'parts': [{'text': 'second'}], 'role': 'model'}), protos.Content({'parts': [{'text': 'What things do I like?.'}], 'role': 'user'}), protos.Content({'parts': [{'text': 'third'}], 'role': 'model'})]
            )"""
        )
        self.assertEqual(expected, result)

    def test_repr_for_incomplete_streaming_chat(self):
        # Multi turn chat
        model = generative_models.GenerativeModel("gemini-pro")
        chat = model.start_chat()

        self.responses["stream_generate_content"] = [
            (chunk for chunk in [simple_response("a"), simple_response("b"), simple_response("c")])
        ]

        msg1 = "I really like fantasy books."
        response = chat.send_message(msg1, stream=True)

        result = repr(chat)
        expected = textwrap.dedent(
            """\
            ChatSession(
                model=genai.GenerativeModel(
                    model_name='models/gemini-pro',
                    generation_config={},
                    safety_settings={},
                    tools=None,
                    system_instruction=None,
                ),
                history=[protos.Content({'parts': [{'text': 'I really like fantasy books.'}], 'role': 'user'}), <STREAMING IN PROGRESS>]
            )"""
        )
        self.assertEqual(expected, result)

    def test_repr_for_broken_streaming_chat(self):
        # Multi turn chat
        model = generative_models.GenerativeModel("gemini-pro")
        chat = model.start_chat()

        self.responses["stream_generate_content"] = [
            (
                chunk
                for chunk in [
                    simple_response("first"),
                    # FinishReason.SAFETY = 3
                    protos.GenerateContentResponse(
                        {
                            "candidates": [
                                {"finish_reason": 3, "content": {"parts": [{"text": "second"}]}}
                            ]
                        }
                    ),
                ]
            )
        ]

        msg1 = "I really like fantasy books."
        response = chat.send_message(msg1, stream=True)

        for chunk in response:
            pass

        result = repr(chat)
        expected = textwrap.dedent(
            """\
            ChatSession(
                model=genai.GenerativeModel(
                    model_name='models/gemini-pro',
                    generation_config={},
                    safety_settings={},
                    tools=None,
                    system_instruction=None,
                ),
                history=[protos.Content({'parts': [{'text': 'I really like fantasy books.'}], 'role': 'user'}), <STREAMING ERROR>]
            )"""
        )
        self.assertEqual(expected, result)

    def test_chat_with_request_options(self):
        self.responses["generate_content"].append(
            protos.GenerateContentResponse(
                {
                    "candidates": [{"finish_reason": "STOP"}],
                }
            )
        )
        request_options = {"timeout": 120}

        model = generative_models.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        chat.send_message("hello", request_options=helper_types.RequestOptions(**request_options))

        request_options["retry"] = None
        self.assertEqual(request_options, self.observed_kwargs[0])

    def test_serialize(self):
        def add(x, y):
            return x + y

        model = generative_models.GenerativeModel(
            model_name=",models/gemini-1.5-flash",
            generation_config={"max_output_tokens": 65},
            tools=[add],
            safety_settings="block_none",
            system_instruction="you are a cat",
        )

        chat = model.start_chat(
            history=[
                {"role": "user", "parts": "hello"},
                {"role": "model", "parts": "meow!"},
                {
                    "role": "user",
                    "parts": [
                        "what's this picture?",
                        {"mime_type": "image/png", "data": b"PNG!"},
                    ],
                },
            ]
        )

        chat_json = chat.to_dict()

        new_chat = generative_models.ChatSession.from_dict(chat_json)

        new_chat_json = chat.to_dict()

        self.assertEqual(chat_json, new_chat_json)


if __name__ == "__main__":
    absltest.main()
