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
        
        @add_client_method
        async def query_corpus(
            request: glm.QueryCorpusRequest,
        ) -> glm.QueryCorpusResponse:
            self.observed_requests.append(request)
            return glm.QueryCorpusResponse(
                relevant_chunks=[
                    glm.RelevantChunk(
                        chunk_relevance_score=0.08,
                        chunk=glm.Chunk(
                            name="corpora/demo_corpus/documents/demo_doc/chunks/demo_chunk",
                            data={"string_value": "This is a demo chunk."},
                        ),
                    )
                ]
            )
        
        @add_client_method
        async def delete_corpus(request: glm.DeleteCorpusRequest) -> None:
            self.observed_requests.append(request)

        @add_client_method
        async def create_document(
            request: glm.CreateDocumentRequest,
        ) -> retriever_service.Document:
            self.observed_requests.append(request)
            return glm.Document(
                name="corpora/demo_corpus/documents/demo_doc", display_name="demo_doc"
            )
        
        @add_client_method
        async def get_document(
            request: glm.GetDocumentRequest,
        ) -> retriever_service.Document:
            self.observed_requests.append(request)
            return glm.Document(
                name="corpora/demo_corpus/documents/demo_doc", display_name="demo_doc"
            )

        @add_client_method
        async def update_document(
            request: glm.UpdateDocumentRequest,
        ) -> glm.Document:
            self.observed_requests.append(request)
            return glm.Document(
                name="corpora/demo_corpus/documents/demo_doc", display_name="demo_doc_1"
            )
        
        @add_client_method
        async def list_documents(
            request: glm.ListDocumentsRequest,
        ) -> glm.ListDocumentsResponse:
            self.observed_requests.append(request)
            return [
                glm.Document(
                    name="corpora/demo_corpus/documents/demo_doc_1", display_name="demo_doc_1"
                ),
                glm.Document(
                    name="corpora/demo_corpus/documents/demo_doc_2", display_name="demo_doc_2"
                ),
            ]

        @add_client_method
        async def delete_document(
            request: glm.DeleteDocumentRequest,
        ) -> None:
            self.observed_requests.append(request)

        @add_client_method
        async def query_document(
            request: glm.QueryDocumentRequest,
        ) -> glm.QueryDocumentResponse:
            self.observed_requests.append(request)
            return glm.QueryCorpusResponse(
                relevant_chunks=[
                    glm.RelevantChunk(
                        chunk_relevance_score=0.08,
                        chunk=glm.Chunk(
                            name="corpora/demo_corpus/documents/demo_doc/chunks/demo_chunk",
                            data={"string_value": "This is a demo chunk."},
                        ),
                    )
                ]
            )

        @add_client_method
        async def create_chunk(
            request: glm.CreateChunkRequest,
        ) -> retriever_service.Chunk:
            self.observed_requests.append(request)
            return glm.Chunk(
                name="corpora/demo_corpus/documents/demo_doc/chunks/demo_chunk",
                data={"string_value": "This is a demo chunk."},
            )
        
        @add_client_method
        async def batch_create_chunks(
            request: glm.BatchCreateChunksRequest,
        ) -> glm.BatchCreateChunksResponse:
            self.observed_requests.append(request)
            return glm.BatchCreateChunksResponse(
                chunks=[
                    glm.Chunk(
                        name="corpora/demo_corpus/documents/demo_doc/chunks/dc",
                        data={"string_value": "This is a demo chunk."},
                    ),
                    glm.Chunk(
                        name="corpora/demo_corpus/documents/demo_doc/chunks/dc1",
                        data={"string_value": "This is another demo chunk."},
                    ),
                ]
            )

        @add_client_method
        async def get_chunk(
            request: glm.GetChunkRequest,
        ) -> retriever_service.Chunk:
            self.observed_requests.append(request)
            return glm.Chunk(
                name="corpora/demo_corpus/documents/demo_doc/chunks/demo_chunk",
                data={"string_value": "This is a demo chunk."},
            )
        
        @add_client_method
        async def list_chunks(
            request: glm.ListChunksRequest,
        ) -> glm.ListChunksResponse:
            self.observed_requests.append(request)
            return [
                glm.Chunk(
                    name="corpora/demo_corpus/documents/demo_doc/chunks/demo_chunk",
                    data={"string_value": "This is a demo chunk."},
                ),
                glm.Chunk(
                    name="corpora/demo_corpus/documents/demo_doc/chunks/demo_chunk_1",
                    data={"string_value": "This is another demo chunk."},
                ),
            ]

        @add_client_method
        async def update_chunk(request: glm.UpdateChunkRequest) -> glm.Chunk:
            self.observed_requests.append(request)
            return glm.Chunk(
                name="corpora/demo_corpus/documents/demo_doc/chunks/demo_chunk",
                data={"string_value": "This is an updated demo chunk."},
            )
        
        @add_client_method
        async def batch_update_chunks(
            request: glm.BatchUpdateChunksRequest,
        ) -> glm.BatchUpdateChunksResponse:
            self.observed_requests.append(request)
            return glm.BatchUpdateChunksResponse(
                chunks=[
                    glm.Chunk(
                        name="corpora/demo_corpus/documents/demo_doc/chunks/demo_chunk",
                        data={"string_value": "This is an updated chunk."},
                    ),
                    glm.Chunk(
                        name="corpora/demo_corpus/documents/demo_doc/chunks/demo_chunk_1",
                        data={"string_value": "This is another updated chunk."},
                    ),
                ]
            )
        
        @add_client_method
        async def delete_chunk(
            request: glm.DeleteChunkRequest,
        ) -> None:
            self.observed_requests.append(request)

        @add_client_method
        async def batch_delete_chunks(
            request: glm.BatchDeleteChunksRequest,
        ) -> None:
            self.observed_requests.append(request)