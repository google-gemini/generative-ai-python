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
import datetime
import dataclasses
import pytz
from typing import Any
import unittest
from unittest import mock

from absl.testing import absltest
from absl.testing import parameterized

import google.ai.generativelanguage as glm

from google.generativeai import models
from google.generativeai import client
from google.generativeai.types import model_types
from google.protobuf import field_mask_pb2


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

        @add_client_method
        def update_tuned_model(
            tuned_model: glm.TunedModel, field_mask: field_mask_pb2.FieldMask
        ):
            request = glm.UpdateTunedModelRequest(
                tuned_model=tuned_model, update_mask=field_mask
            )
            self.observed_requests.append(request)
            response = self.responses.get("update_tuned_model", None)
            if response is None:
                response = tuned_model
            return response

        @add_client_method
        def delete_tuned_model(name):
            request = glm.DeleteTunedModelRequest(name=name)
            self.observed_requests.append(request)
            response = True
            return response

    def test_decode_tuned_model_time_round_trip(self):
        example_dt = datetime.datetime(2000, 1, 2, 3, 4, 5, 600000, pytz.UTC)
        tuned_model = glm.TunedModel(
            name="tunedModels/house-mouse-001", create_time=example_dt
        )
        tuned_model = model_types.decode_tuned_model(tuned_model)
        self.assertEqual(tuned_model.create_time, example_dt)

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

    @parameterized.named_parameters(
        [
            "edited-glm-model",
            glm.TunedModel(
                name="tunedModels/my-pig-001",
                description="Trained on my data",
            ),
            None,
        ],
        [
            "name-and-dict",
            "tunedModels/my-pig-001",
            {"description": "Trained on my data"},
        ],
        [
            "name-and-glm-model",
            "tunedModels/my-pig-001",
            glm.TunedModel(description="Trained on my data"),
        ],
    )
    def test_update_tuned_model_basics(self, tuned_model, updates):
        self.responses["get_tuned_model"] = glm.TunedModel(
            name="tunedModels/my-pig-001"
        )
        # No self.responses['update_tuned_model'] the mock just returns the input.
        updated_model = models.update_tuned_model(tuned_model, updates)
        updated_model.description = "Trained on my data"

    @parameterized.named_parameters(
        [
            "glm-model",
            glm.TunedModel(tuning_task={"hyperparameters": {"batch_size": 8}}),
        ],
        [
            "dict",
            {"tuning_task": {"hyperparameters": {"batch_size": 8}}},
        ],
        [
            "flat-dict",
            {"tuning_task.hyperparameters.batch_size": 8},
        ],
    )
    def test_update_tuned_model_nested_fields(self, updates):
        self.responses["get_tuned_model"] = glm.TunedModel(
            name="tunedModels/my-pig-001", base_model="models/dance-monkey-007"
        )

        result = models.update_tuned_model("tunedModels/my-pig-001", updates)
        self.assertEqual(
            result,
            model_types.TunedModel(
                name="tunedModels/my-pig-001",
                base_model="models/dance-monkey-007",
                tuning_task={"hyperparameters": {"batch_size": 8}, "snapshots": []},
            ),
        )

    @parameterized.named_parameters(
        ["name", "tunedModels/bipedal-pangolin-223"],
        [
            "glm.TunedModel",
            glm.TunedModel(name="tunedModels/bipedal-pangolin-223"),
        ],
        [
            "models.TunedModel",
            model_types.TunedModel(name="tunedModels/bipedal-pangolin-223"),
        ],
    )
    def test_delete_tuned_model(self, model):
        models.delete_tuned_model(model)
        self.assertEqual(
            self.observed_requests[0].name, "tunedModels/bipedal-pangolin-223"
        )


if __name__ == "__main__":
    absltest.main()
