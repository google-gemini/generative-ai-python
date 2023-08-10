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
import copy
import dataclasses
from typing import Any
import unittest
from unittest import mock

from absl.testing import absltest
from absl.testing import parameterized

import google.ai.generativelanguage as glm

from google.generativeai import models
from google.generativeai import client
from google.generativeai.types import model_types


class UnitTests(parameterized.TestCase):
    def setUp(self):
        self.client = unittest.mock.MagicMock()

        client.default_model_client = self.client

        def add_client_method(f):
            name = f.__name__
            setattr(self.client, name, f)
            return f

        self.observed_requests = []
        self.responses = {}

        @add_client_method
        def get_model(
            request: glm.GetModelRequest | None = None, *, name=None
        ) -> glm.Model:
            if request is None:
                request = glm.GetModelRequest(name=name)
            self.assertIsInstance(request, glm.GetModelRequest)
            self.observed_requests.append(request)
            response = copy.copy(self.responses["get_model"])
            return response

        @add_client_method
        def get_tuned_model(
            request: glm.GetTunedModelRequest | None = None, *, name=None
        ) -> glm.TunedModel:
            if request is None:
                request = glm.GetTunedModelRequest(name=name)
            self.assertIsInstance(request, glm.GetTunedModelRequest)
            self.observed_requests.append(request)
            response = copy.copy(self.responses["get_tuned_model"])
            return response

        @dataclasses.dataclass
        class ListWrapper:
            _response: Any

        @add_client_method
        def list_models(
            request: glm.ListModelsRequest = None, *, page_size=None, page_token=None
        ) -> glm.ListModelsResponse:
            if request is None:
                request = glm.ListModelsRequest(
                    page_size=page_size, page_token=page_token
                )
            self.assertIsInstance(request, glm.ListModelsRequest)
            self.observed_requests.append(request)
            response = self.responses["list_models"][request.page_token]
            return ListWrapper(response)

        @add_client_method
        def list_tuned_models(
            request: glm.ListTunedModelsRequest = None,
            *,
            page_size=None,
            page_token=None
        ) -> glm.ListModelsResponse:
            if request is None:
                request = glm.ListTunedModelsRequest(
                    page_size=page_size, page_token=page_token
                )
            self.assertIsInstance(request, glm.ListTunedModelsRequest)
            self.observed_requests.append(request)
            response = self.responses["list_tuned_models"][request.page_token]
            return ListWrapper(response)

    @parameterized.named_parameters(
        ["simple", "models/fake-bison-001"],
        ["simple-tuned", "tunedModels/my-pig-001"],
        ["model-instance", glm.Model(name="models/fake-bison-001")],
        ["tuned-model-instance", glm.TunedModel(name="tunedModels/my-pig-001")],
    )
    def test_get_model(self, name):
        self.responses = {
            "get_model": glm.Model(name="models/fake-bison-001"),
            "get_tuned_model": glm.TunedModel(name="tunedModels/my-pig-001"),
        }

        model = models.get_model(name)
        if self.observed_requests[0].name.startswith("models/"):
            self.assertIsInstance(model, model_types.Model)
        else:
            self.assertIsInstance(model, model_types.TunedModel)

    @parameterized.named_parameters(
        ["simple", "mystery-bison-001"],
        ["model-instance", glm.Model(name="how?-bison-001")],
    )
    def test_fail_with_unscoped_model_name(self, name):
        with self.assertRaises(ValueError):
            model = models.get_model(name)

    def test_list_models(self):
        self.responses = {
            "list_models": {
                # The first request doesn't pass a page token
                "": glm.ListModelsResponse(
                    models=[
                        glm.Model(name="models/fake-bison-001"),
                        glm.Model(name="models/fake-bison-002"),
                    ],
                    next_page_token="page1",
                ),
                "page1": glm.ListModelsResponse(
                    models=[
                        glm.Model(name="models/fake-bison-003"),
                    ],
                    # The last page returns an empty page token.
                    next_page_token="",
                ),
            }
        }

        found_models = list(models.list_models())
        self.assertLen(found_models, 3)
        for m in found_models:
            self.assertIsInstance(m, model_types.Model)

    def test_list_tuned_models(self):
        self.responses = {
            "list_tuned_models": {
                # The first request doesn't pass a page token
                "": glm.ListTunedModelsResponse(
                    tuned_models=[
                        glm.TunedModel(name="tunedModels/my-pig-001"),
                        glm.TunedModel(name="tunedModels/my-pig-002"),
                    ],
                    next_page_token="page1",
                ),
                "page1": glm.ListTunedModelsResponse(
                    tuned_models=[
                        glm.TunedModel(name="tunedModels/my-pig-003"),
                    ],
                    # The last page returns an empty page token.
                    next_page_token="",
                ),
            }
        }
        found_models = list(models.list_tuned_models())
        self.assertLen(found_models, 3)
        for m in found_models:
            self.assertIsInstance(m, model_types.TunedModel)


if __name__ == "__main__":
    absltest.main()
