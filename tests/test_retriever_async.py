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
import collections
import copy
import math
import unittest
import unittest.mock as mock

import google.ai.generativelanguage as glm

from google.generativeai import retriever
from google.generativeai import client
from google.generativeai.types import retriever_types as retriever_service
from absl.testing import absltest
from absl.testing import parameterized


class AsyncTests(parameterized.TestCase, unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = unittest.mock.MagicMock()

        client._client_manager.clients["retriever_async"] = self.client

        def add_client_method(f):
            name = f.__name__
            setattr(self.client, name, f)
            return f

        self.observed_requests = []
        self.responses = collections.defaultdict(list)

        @add_client_method
        async def create_corpus(
            request: glm.CreateCorpusRequest,
        ) -> glm.Corpus:
            self.observed_requests.append(request)
            return glm.Corpus(name="corpora/demo_corpus", display_name="demo_corpus")

        @add_client_method
        async def get_corpus(
            request: glm.GetCorpusRequest,
        ) -> glm.Corpus:
            self.observed_requests.append(request)
            return glm.Corpus(name="corpora/demo_corpus", display_name="demo_corpus")

        @add_client_method
        async def update_corpus(request: glm.UpdateCorpusRequest) -> glm.Corpus:
            self.observed_requests.append(request)
            return glm.Corpus(name="corpora/demo_corpus", display_name="demo_corpus_1")

        @add_client_method
        async def list_corpora(request: glm.ListCorporaRequest) -> glm.ListCorporaResponse:
            self.observed_requests.append(request)
            return [
                glm.Corpus(name="corpora/demo_corpus_1", display_name="demo_corpus_1"),
                glm.Corpus(name="corpora/demo_corpus_2", display_name="demo_corpus_2"),
            ]
