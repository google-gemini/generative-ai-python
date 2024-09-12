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
import collections
from typing import Union

from absl.testing import absltest
from absl.testing import parameterized

from google.generativeai import protos

from google.generativeai import client
from google.generativeai import models
from google.generativeai.types import model_types
from google.generativeai.types import helper_types

from google.api_core import retry


class MockModelClient:
    def __init__(self, test):
        self.test = test

    def get_model(
        self,
        request: Union[protos.GetModelRequest, None] = None,
        *,
        name=None,
        timeout=None,
        retry=None
    ) -> protos.Model:
        if request is None:
            request = protos.GetModelRequest(name=name)
        self.test.assertIsInstance(request, protos.GetModelRequest)
        self.test.observed_requests.append(request)
        self.test.observed_timeout.append(timeout)
        self.test.observed_retry.append(retry)
        response = copy.copy(self.test.responses["get_model"])
        return response


class HelperTests(parameterized.TestCase):

    def setUp(self):
        self.client = MockModelClient(self)
        client._client_manager.clients["model"] = self.client

        self.observed_requests = []
        self.observed_retry = []
        self.observed_timeout = []
        self.responses = collections.defaultdict(list)

    @parameterized.named_parameters(
        ["None", None, None, None],
        ["Empty", {}, None, None],
        ["Timeout", {"timeout": 7}, 7, None],
        ["Retry", {"retry": retry.Retry(timeout=7)}, None, retry.Retry(timeout=7)],
        [
            "RequestOptions",
            helper_types.RequestOptions(timeout=7, retry=retry.Retry(multiplier=3)),
            7,
            retry.Retry(multiplier=3),
        ],
    )
    def test_get_model(self, request_options, expected_timeout, expected_retry):
        self.responses = {"get_model": protos.Model(name="models/fake-bison-001")}

        _ = models.get_model("models/fake-bison-001", request_options=request_options)

        self.assertEqual(self.observed_timeout[0], expected_timeout)
        self.assertEqual(str(self.observed_retry[0]), str(expected_retry))


if __name__ == "__main__":
    absltest.main()
