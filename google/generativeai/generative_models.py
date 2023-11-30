"""Classes for working with the Gemini models."""

from __future__ import annotations

import dataclasses

# pylint: disable=bad-continuation, line-too-long


from collections.abc import Iterable

from google.ai import generativelanguage as glm
from google.generativeai import client
from google.generativeai.types import content_types
from google.generativeai.types import generation_types
from google.generativeai.types import safety_types


class GenerativeModel:
    def __init__(
        self,
        model_name: str = "gemini-m",
        safety_settings: safety_types.SafetySettingOptions | None = None,
        generation_config: generation_types.GenerationConfigType | None = None,
    ):
        if "/" not in model_name:
            model_name = "models/" + model_name
        self._model_name = model_name
        self._safety_settings = safety_types.to_easy_safety_dict(
            safety_settings, harm_category_set="new"
        )
        self._generation_config = generation_types.to_generation_config_dict(generation_config)
        self._client = client.get_default_generative_client()
        # self._async_client = client.get_default_generative_async_client()

    @property
    def model_name(self):
        return self._model_name

    def __str__(self):
        return f"genai.GenerativeModel(model_name='{self.model_name}', ...)"

    def _prepare_request(
        self,
        *,
        contents: (content_types.ContentOptions | Iterable[content_types.StrictContentOptions]),
        generation_config: generation_types.GenerationConfigType | None = None,
        safety_settings: safety_types.SafetySettingOptions | None = None,
    ) -> glm.GenerateContentRequest:
        if not contents:
            raise TypeError("contents must not be empty")

        contents = content_types.to_contents(contents)

        generation_config = generation_types.to_generation_config_dict(generation_config)
        merged_gc = self._generation_config.copy()
        merged_gc.update(generation_config)

        safety_settings = safety_types.to_easy_safety_dict(safety_settings, harm_category_set="new")
        merged_ss = self._safety_settings.copy()
        merged_ss.update(safety_settings)
        merged_ss = safety_types.normalize_safety_settings(merged_ss, harm_category_set="new")

        return glm.GenerateContentRequest(
            model=self._model_name,
            contents=contents,
            generation_config=merged_gc,
            safety_settings=merged_ss,
        )

    def generate_content(
        self,
        contents: (content_types.ContentOptions | Iterable[content_types.StrictContentOptions]),
        *,
        generation_config: generation_types.GenerationConfigType | None = None,
        safety_settings: safety_types.SafetySettingOptions | None = None,
        stream: bool = False,
    ) -> generation_types.GenerateContentResponse:
        request = self._prepare_request(
            contents=contents,
            generation_config=generation_config,
            safety_settings=safety_settings,
        )

        if stream:
            iterator = self._client.stream_generate_content(request)
            return generation_types.GenerateContentResponse.from_iterator(iterator)
        else:
            response = self._client.generate_content(request)
            return generation_types.GenerateContentResponse.from_response(response)

    def start_chat(
        self,
        *,
        history: Iterable[content_types.StrictContentOptions] | None = None,
    ) -> ChatSession:
        if self._generation_config.get("candidate_count", 1) > 1:
            raise ValueError("Can't chat with `candidate_count > 1`")
        return ChatSession(
            model=self,
            history=history,
        )


class ChatSession:
    _USER_ROLE = "user"
    _MODEL_ROLE = "model"

    def __init__(
        self,
        model: GenerativeModel,
        history: Iterable[content_types.StrictContentOptions] | None = None,
    ):
        self.model: GenerativeModel = model
        self._history: list[glm.Content] = content_types.to_contents(history)
        self._last_sent: glm.Content | None = None
        self._last_received: generation_types.GenerateContentResponse | None = None

    def send_message(
        self,
        content: content_types.ContentOptions,
        *,
        generation_config: generation_types.GenerationConfigType = None,
        safety_settings: safety_types.SafetySettingOptions = None,
        stream: bool = False,
    ) -> generation_types.GenerateContentResponse:
        content = content_types.to_content(content)
        if not content.role:
            content.role = self._USER_ROLE
        history = self.history[:]
        history.append(content)

        generation_config = generation_types.to_generation_config_dict(generation_config)
        if generation_config.get("candidate_count", 1) > 1:
            raise ValueError("Can't chat with `candidate_count > 1`")
        response = self.model.generate_content(
            contents=history,
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=stream,
        )

        if response.prompt_feedback.block_reason:
            raise generation_types.BlockedPromptException(response.prompt_feedback)

        if not stream:
            if response.candidates[0].finish_reason not in (
                glm.Candidate.FinishReason.FINISH_REASON_UNSPECIFIED,
                glm.Candidate.FinishReason.STOP,
                glm.Candidate.FinishReason.MAX_TOKENS,
            ):
                raise generation_types.StopCandidateException(response.candidates[0])

        self._last_sent = content
        self._last_received = response

        return response

    def __copy__(self):
        return ChatSession(
            model=self.model,
            # Be sure the copy doesn't share the history.
            history=list(self.history),
        )

    def rewind(self) -> tuple[glm.Content, glm.Content]:
        """Removes the last request/response pair from the chat history."""
        if self._last_received is None:
            result = self._history.pop(-2), self._history.pop()
            return result
        else:
            result = self._last_sent, self._last_received.candidates[0].content
            self._last_sent = None
            self._last_received = None
            return result

    @property
    def last(self):
        return self._last_received

    @property
    def history(self):
        last = self._last_received
        if last is None:
            return self._history

        if last.candidates[0].finish_reason not in (
            glm.Candidate.FinishReason.FINISH_REASON_UNSPECIFIED,
            glm.Candidate.FinishReason.STOP,
            glm.Candidate.FinishReason.MAX_TOKENS,
        ):
            error = generation_types.StopCandidateException(last.candidates[0])
            last._error = error

        if last._error is not None:
            raise generation_types.BrokenResponseError(
                "Can not build a coherent char history after a broken "
                "streaming response "
                "(See the previous Exception fro details). "
                "To inspect the last response object, use `chat.last`."
                "To remove the last request/response `Content` objects from the chat "
                "call `last_send, last_received = chat.rewind()` and continue "
                "without it."
            ) from last._error

        sent = self._last_sent
        received = self._last_received.candidates[0].content
        if not received.role:
            received.role = self._MODEL_ROLE
        self._history.extend([sent, received])

        self._last_sent = None
        self._last_received = None

        return self._history

    @history.setter
    def history(self, history):
        self._history = content_types.to_contents(history)
        self._last_self = None
        self._last_received = None
