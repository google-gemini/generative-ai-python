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
from typing import Any
import unittest
import unittest.mock as mock

from google.generativeai import protos

from google.generativeai import retriever
from google.generativeai import client
from google.generativeai.types import retriever_types as retriever_service
from absl.testing import absltest
from absl.testing import parameterized


class UnitTests(parameterized.TestCase):
    def setUp(self):
        self.client = unittest.mock.MagicMock()

        client._client_manager.clients["retriever"] = self.client

        self.observed_requests = []

        self.responses = {}

        def add_client_method(f):
            name = f.__name__
            setattr(self.client, name, f)
            return f

        @add_client_method
        def create_corpus(
            request: protos.CreateCorpusRequest,
            **kwargs,
        ) -> protos.Corpus:
            self.observed_requests.append(request)
            return protos.Corpus(
                name="corpora/demo_corpus",
                display_name="demo-corpus",
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def get_corpus(
            request: protos.GetCorpusRequest,
            **kwargs,
        ) -> protos.Corpus:
            self.observed_requests.append(request)
            return protos.Corpus(
                name="corpora/demo_corpus",
                display_name="demo-corpus",
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def update_corpus(
            request: protos.UpdateCorpusRequest,
            **kwargs,
        ) -> protos.Corpus:
            self.observed_requests.append(request)
            return protos.Corpus(
                name="corpora/demo-corpus",
                display_name="demo-corpus-1",
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def list_corpora(
            request: protos.ListCorporaRequest,
            **kwargs,
        ) -> protos.ListCorporaResponse:
            self.observed_requests.append(request)
            return [
                protos.Corpus(
                    name="corpora/demo_corpus-1",
                    display_name="demo-corpus-1",
                    create_time="2000-01-01T01:01:01.123456Z",
                    update_time="2000-01-01T01:01:01.123456Z",
                ),
                protos.Corpus(
                    name="corpora/demo-corpus-2",
                    display_name="demo-corpus-2",
                    create_time="2000-01-01T01:01:01.123456Z",
                    update_time="2000-01-01T01:01:01.123456Z",
                ),
            ]

        @add_client_method
        def query_corpus(
            request: protos.QueryCorpusRequest,
            **kwargs,
        ) -> protos.QueryCorpusResponse:
            self.observed_requests.append(request)
            return protos.QueryCorpusResponse(
                relevant_chunks=[
                    protos.RelevantChunk(
                        chunk_relevance_score=0.08,
                        chunk=protos.Chunk(
                            name="corpora/demo-corpus/documents/demo-doc/chunks/demo-chunk",
                            data={"string_value": "This is a demo chunk."},
                            custom_metadata=[],
                            state=0,
                            create_time="2000-01-01T01:01:01.123456Z",
                            update_time="2000-01-01T01:01:01.123456Z",
                        ),
                    )
                ]
            )

        @add_client_method
        def delete_corpus(
            request: protos.DeleteCorpusRequest,
            **kwargs,
        ) -> None:
            self.observed_requests.append(request)

        @add_client_method
        def create_document(
            request: protos.CreateDocumentRequest,
            **kwargs,
        ) -> retriever_service.Document:
            self.observed_requests.append(request)
            return protos.Document(
                name="corpora/demo-corpus/documents/demo-doc",
                display_name="demo-doc",
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def get_document(
            request: protos.GetDocumentRequest,
            **kwargs,
        ) -> retriever_service.Document:
            self.observed_requests.append(request)
            return protos.Document(
                name="corpora/demo-corpus/documents/demo_doc",
                display_name="demo-doc",
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def update_document(
            request: protos.UpdateDocumentRequest,
            **kwargs,
        ) -> protos.Document:
            self.observed_requests.append(request)
            return protos.Document(
                name="corpora/demo-corpus/documents/demo_doc",
                display_name="demo-doc-1",
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def list_documents(
            request: protos.ListDocumentsRequest,
            **kwargs,
        ) -> protos.ListDocumentsResponse:
            self.observed_requests.append(request)
            return [
                protos.Document(
                    name="corpora/demo-corpus/documents/demo_doc_1",
                    display_name="demo-doc-1",
                    create_time="2000-01-01T01:01:01.123456Z",
                    update_time="2000-01-01T01:01:01.123456Z",
                ),
                protos.Document(
                    name="corpora/demo-corpus/documents/demo_doc_2",
                    display_name="demo-doc-2",
                    create_time="2000-01-01T01:01:01.123456Z",
                    update_time="2000-01-01T01:01:01.123456Z",
                ),
            ]

        @add_client_method
        def delete_document(
            request: protos.DeleteDocumentRequest,
            **kwargs,
        ) -> None:
            self.observed_requests.append(request)

        @add_client_method
        def query_document(
            request: protos.QueryDocumentRequest,
            **kwargs,
        ) -> protos.QueryDocumentResponse:
            self.observed_requests.append(request)
            return protos.QueryDocumentResponse(
                relevant_chunks=[
                    protos.RelevantChunk(
                        chunk_relevance_score=0.08,
                        chunk=protos.Chunk(
                            name="demo-chunk",
                            data={"string_value": "This is a demo chunk."},
                            custom_metadata=[],
                            state=0,
                            create_time="2000-01-01T01:01:01.123456Z",
                            update_time="2000-01-01T01:01:01.123456Z",
                        ),
                    )
                ]
            )

        @add_client_method
        def create_chunk(
            request: protos.CreateChunkRequest,
            **kwargs,
        ) -> retriever_service.Chunk:
            self.observed_requests.append(request)
            return protos.Chunk(
                name="corpora/demo-corpus/documents/dem-doc/chunks/demo-chunk",
                data={"string_value": "This is a demo chunk."},
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def batch_create_chunks(
            request: protos.BatchCreateChunksRequest,
            **kwargs,
        ) -> protos.BatchCreateChunksResponse:
            self.observed_requests.append(request)
            return protos.BatchCreateChunksResponse(
                chunks=[
                    protos.Chunk(
                        name="corpora/demo-corpus/documents/demo-doc/chunks/dc",
                        data={"string_value": "This is a demo chunk."},
                        create_time="2000-01-01T01:01:01.123456Z",
                        update_time="2000-01-01T01:01:01.123456Z",
                    ),
                    protos.Chunk(
                        name="corpora/demo-corpus/documents/demo-doc/chunks/dc1",
                        data={"string_value": "This is another demo chunk."},
                        create_time="2000-01-01T01:01:01.123456Z",
                        update_time="2000-01-01T01:01:01.123456Z",
                    ),
                ]
            )

        @add_client_method
        def get_chunk(
            request: protos.GetChunkRequest,
            **kwargs,
        ) -> retriever_service.Chunk:
            self.observed_requests.append(request)
            return protos.Chunk(
                name="corpora/demo-corpus/documents/dem-doc/chunks/demo-chunk",
                data={"string_value": "This is a demo chunk."},
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def list_chunks(
            request: protos.ListChunksRequest,
            **kwargs,
        ) -> protos.ListChunksResponse:
            self.observed_requests.append(request)
            return [
                protos.Chunk(
                    name="corpora/demo-corpus/documents/dem-doc/chunks/demo-chunk",
                    data={"string_value": "This is a demo chunk."},
                    create_time="2000-01-01T01:01:01.123456Z",
                    update_time="2000-01-01T01:01:01.123456Z",
                ),
                protos.Chunk(
                    name="corpora/demo-corpus/documents/demo-doc/chunks/demo-chunk-1",
                    data={"string_value": "This is another demo chunk."},
                    create_time="2000-01-01T01:01:01.123456Z",
                    update_time="2000-01-01T01:01:01.123456Z",
                ),
            ]

        @add_client_method
        def update_chunk(
            request: protos.UpdateChunkRequest,
            **kwargs,
        ) -> protos.Chunk:
            self.observed_requests.append(request)
            return protos.Chunk(
                name="corpora/demo-corpus/documents/dem-doc/chunks/demo-chunk",
                data={"string_value": "This is an updated demo chunk."},
                custom_metadata=[
                    protos.CustomMetadata(
                        key="tags",
                        string_list_value=protos.StringList(
                            values=["Google For Developers", "Project IDX", "Blog", "Announcement"]
                        ),
                    )
                ],
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def batch_update_chunks(
            request: protos.BatchUpdateChunksRequest,
            **kwargs,
        ) -> protos.BatchUpdateChunksResponse:
            self.observed_requests.append(request)
            return protos.BatchUpdateChunksResponse(
                chunks=[
                    protos.Chunk(
                        name="corpora/demo-corpus/documents/dem-doc/chunks/demo-chunk",
                        data={"string_value": "This is an updated chunk."},
                        create_time="2000-01-01T01:01:01.123456Z",
                        update_time="2000-01-01T01:01:01.123456Z",
                    ),
                    protos.Chunk(
                        name="corpora/demo-corpus/documents/demo-doc/chunks/demo-chunk-1",
                        data={"string_value": "This is another updated chunk."},
                        create_time="2000-01-01T01:01:01.123456Z",
                        update_time="2000-01-01T01:01:01.123456Z",
                    ),
                ]
            )

        @add_client_method
        def delete_chunk(
            request: protos.DeleteChunkRequest,
            **kwargs,
        ) -> None:
            self.observed_requests.append(request)

        @add_client_method
        def batch_delete_chunks(
            request: protos.BatchDeleteChunksRequest,
            **kwargs,
        ) -> None:
            self.observed_requests.append(request)

    def test_create_corpus(self, name="demo-corpus"):
        x = retriever.create_corpus(name=name)
        self.assertIsInstance(x, retriever_service.Corpus)
        self.assertEqual("demo-corpus", x.display_name)
        self.assertEqual("corpora/demo_corpus", x.name)

    def test_create_corpus_no_name(self):
        x = retriever.create_corpus()
        self.assertIsInstance(x, retriever_service.Corpus)
        self.assertEqual("demo-corpus", x.display_name)
        self.assertEqual("corpora/demo_corpus", x.name)

    def test_get_corpus(self, name="demo-corpus"):
        x = retriever.create_corpus(name=name)
        c = retriever.get_corpus(name=x.name)
        self.assertEqual("demo-corpus", c.display_name)

    def test_update_corpus(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        update_request = demo_corpus.update(updates={"display_name": "demo-corpus_1"})
        self.assertIsInstance(self.observed_requests[-1], protos.UpdateCorpusRequest)
        self.assertEqual("demo-corpus_1", demo_corpus.display_name)

    def test_list_corpora(self):
        x = list(retriever.list_corpora(page_size=1))
        self.assertEqual(len(x), 2)

    def test_query_corpus(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        demo_chunk = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        q = demo_corpus.query(query="What kind of chunk is this?")
        self.assertEqual(
            q,
            [
                retriever_service.RelevantChunk(
                    chunk_relevance_score=0.08,
                    chunk=retriever_service.Chunk(
                        name="corpora/demo-corpus/documents/demo-doc/chunks/demo-chunk",
                        data="This is a demo chunk.",
                        custom_metadata=[],
                        state=0,
                        create_time="2000-01-01T01:01:01.123456Z",
                        update_time="2000-01-01T01:01:01.123456Z",
                    ),
                )
            ],
        )

    def test_delete_corpus(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        delete_request = retriever.delete_corpus(name="corpora/demo_corpus", force=True)
        self.assertIsInstance(self.observed_requests[-1], protos.DeleteCorpusRequest)

    def test_create_document(self, display_name="demo-doc"):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        x = demo_corpus.create_document(name=display_name)
        self.assertIsInstance(x, retriever_service.Document)
        self.assertEqual("demo-doc", x.display_name)

    def test_create_document_no_name(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        x = demo_corpus.create_document()
        self.assertIsInstance(x, retriever_service.Document)
        self.assertEqual("demo-doc", x.display_name)

    def test_get_document(self, display_name="demo-doc"):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        x = demo_corpus.create_document(name=display_name)
        d = demo_corpus.get_document(name=x.name)
        self.assertEqual("demo-doc", d.display_name)

    def test_update_document(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        update_request = demo_document.update(updates={"display_name": "demo-doc-1"})
        self.assertEqual("demo-doc-1", demo_document.display_name)

    def test_delete_document(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        demo_doc2 = demo_corpus.create_document(name="demo-doc-2")
        delete_request = demo_corpus.delete_document(name="corpora/demo-corpus/documents/demo_doc")
        self.assertIsInstance(self.observed_requests[-1], protos.DeleteDocumentRequest)

    def test_list_documents(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        demo_doc2 = demo_corpus.create_document(name="demo-doc-2")
        self.assertLen(list(demo_corpus.list_documents()), 2)

    def test_query_document(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        demo_chunk = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        q = demo_document.query(query="What kind of chunk is this?")
        self.assertEqual(
            q,
            [
                retriever_service.RelevantChunk(
                    chunk_relevance_score=0.08,
                    chunk=retriever_service.Chunk(
                        name="demo-chunk",
                        data="This is a demo chunk.",
                        custom_metadata=[],
                        state=0,
                        create_time="2000-01-01T01:01:01.123456Z",
                        update_time="2000-01-01T01:01:01.123456Z",
                    ),
                )
            ],
        )

    def test_create_chunk(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        self.assertIsInstance(x, retriever_service.Chunk)
        self.assertEqual("corpora/demo-corpus/documents/dem-doc/chunks/demo-chunk", x.name)
        self.assertEqual(retriever_service.ChunkData("This is a demo chunk."), x.data)

    def test_create_chunk_empty(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            data="This is a demo chunk.",
        )
        self.assertIsInstance(x, retriever_service.Chunk)
        self.assertEqual("corpora/demo-corpus/documents/dem-doc/chunks/demo-chunk", x.name)
        self.assertEqual(retriever_service.ChunkData("This is a demo chunk."), x.data)

    @parameterized.named_parameters(
        [
            dict(
                testcase_name="dictionaries",
                chunks=[
                    {
                        "name": "corpora/demo-corpus/documents/demo-doc/chunks/dc",
                        "data": "This is a demo chunk.",
                    },
                    {
                        "name": "corpora/demo-corpus/documents/demo-doc/chunks/dc1",
                        "data": "This is another demo chunk.",
                    },
                ],
            ),
            dict(
                testcase_name="tuples",
                chunks=[
                    (
                        "corpora/demo-corpus/documents/demo-doc/chunks/dc",
                        "This is a demo chunk.",
                    ),
                    (
                        "corpora/demo-corpus/documents/demo-doc/chunks/dc1",
                        "This is another demo chunk.",
                    ),
                ],
            ),
        ]
    )
    def test_batch_create_chunks(self, chunks):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        chunks = demo_document.batch_create_chunks(chunks=chunks)
        self.assertIsInstance(self.observed_requests[-1], protos.BatchCreateChunksRequest)
        self.assertEqual("This is a demo chunk.", chunks[0].data.string_value)
        self.assertEqual("This is another demo chunk.", chunks[1].data.string_value)

    def test_get_chunk(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        ch = demo_document.get_chunk(name=x.name)
        self.assertEqual(retriever_service.ChunkData("This is a demo chunk."), ch.data)

    def test_list_chunks(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        y = demo_document.create_chunk(
            name="demo-chunk-1",
            data="This is another demo chunk.",
        )

        list_req = list(demo_document.list_chunks())
        self.assertIsInstance(self.observed_requests[-1], protos.ListChunksRequest)
        self.assertLen(list_req, 2)

    def test_update_chunk(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
            custom_metadata=[
                retriever_service.CustomMetadata(
                    key="tag",
                    value=[
                        "Google For Developers",
                        "Project IDX",
                        "Blog",
                        "Announcement",
                    ],
                )
            ],
        )
        x.update(updates={"data": {"string_value": "This is an updated demo chunk."}})
        self.assertEqual(
            retriever_service.ChunkData("This is an updated demo chunk."),
            x.data,
        )

    @parameterized.named_parameters(
        [
            dict(
                testcase_name="dictionary_of_updates",
                updates={
                    "corpora/demo-corpus/documents/demo-doc/chunks/demo-chunk": {
                        "data": {"string_value": "This is an updated chunk."}
                    },
                    "corpora/demo-corpus/documents/demo-doc/chunks/demo-chunk-1": {
                        "data": {"string_value": "This is another updated chunk."}
                    },
                },
            ),
            dict(
                testcase_name="list_of_tuples",
                updates=[
                    (
                        "corpora/demo-corpus/documents/demo-doc/chunks/demo-chunk",
                        {"data": {"string_value": "This is an updated chunk."}},
                    ),
                    (
                        "corpora/demo-corpus/documents/demo-doc/chunks/demo-chunk-1",
                        {"data": {"string_value": "This is another updated chunk."}},
                    ),
                ],
            ),
        ],
    )
    def test_batch_update_chunks_data_structures(self, updates):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        y = demo_document.create_chunk(
            name="demo-chunk-1",
            data="This is another demo chunk.",
        )
        update_request = demo_document.batch_update_chunks(chunks=updates)
        self.assertIsInstance(self.observed_requests[-1], protos.BatchUpdateChunksRequest)
        self.assertEqual(
            "This is an updated chunk.", update_request["chunks"][0]["data"]["string_value"]
        )
        self.assertEqual(
            "This is another updated chunk.", update_request["chunks"][1]["data"]["string_value"]
        )

    def test_delete_chunk(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        delete_request = demo_document.delete_chunk(name="demo-chunk")
        self.assertIsInstance(self.observed_requests[-1], protos.DeleteChunkRequest)

    def test_batch_delete_chunks(self):
        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        y = demo_document.create_chunk(
            name="demo-chunk",
            data="This is another demo chunk.",
        )
        delete_request = demo_document.batch_delete_chunks(chunks=[x.name, y.name])
        self.assertIsInstance(self.observed_requests[-1], protos.BatchDeleteChunksRequest)

    @parameterized.parameters(
        {"method": "create_corpus"},
        {"method": "get_corpus"},
        {"method": "delete_corpus"},
    )
    def test_corpus_called_with_request_options(self, method):
        setattr(self.client, method, unittest.mock.MagicMock())
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        try:
            getattr(retriever, method)(name="test", request_options=request_options)
        except AttributeError:
            pass

        getattr(self.client, method).assert_called_once_with(request, **request_options)

    def test_update_corpus_called_with_request_options(self):
        self.client.update_corpus = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        demo_corpus = retriever.create_corpus(name="demo-corpus")
        update_request = demo_corpus.update(updates={}, request_options=request_options)

        self.client.update_corpus.assert_called_once_with(request, **request_options)

    def test_list_corpora_called_with_request_options(self):
        self.client.list_corpora = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        list(retriever.list_corpora(request_options=request_options))
        self.client.list_corpora.assert_called_once_with(request, **request_options)

    def test_query_corpus_called_with_request_options(self):
        self.client.query_corpus = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        demo_chunk = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        try:
            demo_corpus.query(query="What kind of chunk is this?", request_options=request_options)
        except AttributeError:
            pass

        self.client.query_corpus.assert_called_once_with(request, **request_options)

    def test_delete_corpus_called_with_request_options(self):
        self.client.delete_corpus = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        retriever.delete_corpus(name="corpora/demo_corpus", request_options=request_options)
        self.client.delete_corpus.assert_called_once_with(request, **request_options)

    def test_create_document_called_with_request_options(self):
        self.client.create_document = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        try:
            demo_corpus = retriever.create_corpus(name="demo-corpus")
            demo_corpus.create_document(name="demo-doc", request_options=request_options)
        except AttributeError:
            pass

        self.client.create_document.assert_called_once_with(request, **request_options)

    def test_get_document_called_with_request_options(self):
        self.client.get_document = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        try:
            demo_corpus = retriever.create_corpus(name="demo-corpus")
            x = demo_corpus.create_document(name="demo-doc")
            d = demo_corpus.get_document(name=x.name, request_options=request_options)
        except AttributeError:
            pass

        self.client.get_document.assert_called_once_with(request, **request_options)

    def test_update_document_called_with_request_options(self):
        self.client.update_document = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        update_request = demo_document.update(
            updates={"display_name": "demo-doc-1"}, request_options=request_options
        )

        self.client.update_document.assert_called_once_with(request, **request_options)

    def test_list_documents_called_with_request_options(self):
        self.client.list_documents = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        demo_doc2 = demo_corpus.create_document(name="demo-doc-2")
        list(demo_corpus.list_documents(request_options=request_options))

        self.client.list_documents.assert_called_once_with(request, **request_options)

    def test_delete_document_called_with_request_options(self):
        self.client.delete_document = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        demo_doc2 = demo_corpus.create_document(name="demo-doc-2")
        delete_request = demo_corpus.delete_document(
            name="corpora/demo-corpus/documents/demo_doc", request_options=request_options
        )

        self.client.delete_document.assert_called_once_with(request, **request_options)

    def test_query_document_called_with_request_options(self):
        self.client.query_document = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        try:
            demo_corpus = retriever.create_corpus(name="demo-corpus")
            demo_document = demo_corpus.create_document(name="demo-doc")
            demo_chunk = demo_document.create_chunk(
                name="demo-chunk",
                data="This is a demo chunk.",
            )
            q = demo_document.query(
                query="What kind of chunk is this?", request_options=request_options
            )
        except AttributeError:
            pass

        self.client.query_document.assert_called_once_with(request, **request_options)

    def test_create_chunk_called_with_request_options(self):
        self.client.create_chunk = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        try:
            demo_corpus = retriever.create_corpus(name="demo-corpus")
            demo_document = demo_corpus.create_document(name="demo-doc")
            x = demo_document.create_chunk(
                name="demo-chunk", data="This is a demo chunk.", request_options=request_options
            )
        except AttributeError:
            pass

        self.client.create_chunk.assert_called_once_with(request, **request_options)

    def test_batch_create_chunks_called_with_request_options(self):
        self.client.batch_create_chunks = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        chunks = demo_document.batch_create_chunks(
            chunks=[
                (
                    "corpora/demo-corpus/documents/demo-doc/chunks/dc",
                    "This is a demo chunk.",
                ),
                (
                    "corpora/demo-corpus/documents/demo-doc/chunks/dc1",
                    "This is another demo chunk.",
                ),
            ],
            request_options=request_options,
        )

        self.client.batch_create_chunks.assert_called_once_with(request, **request_options)

    def test_get_chunk_called_with_request_options(self):
        self.client.get_chunk = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        try:
            demo_corpus = retriever.create_corpus(name="demo-corpus")
            demo_document = demo_corpus.create_document(name="demo-doc")
            x = demo_document.create_chunk(
                name="demo-chunk",
                data="This is a demo chunk.",
            )
            ch = demo_document.get_chunk(name=x.name, request_options=request_options)
        except AttributeError:
            pass

        self.client.get_chunk.assert_called_once_with(request, **request_options)

    def test_list_chunks_called_with_request_options(self):
        self.client.list_chunks = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        try:
            demo_corpus = retriever.create_corpus(name="demo-corpus")
            demo_document = demo_corpus.create_document(name="demo-doc")
            x = demo_document.create_chunk(
                name="demo-chunk",
                data="This is a demo chunk.",
            )
            y = demo_document.create_chunk(
                name="demo-chunk-1",
                data="This is another demo chunk.",
            )
            list_req = list(demo_document.list_chunks(request_options=request_options))
        except AttributeError:
            pass

        self.client.list_chunks.assert_called_once_with(request, **request_options)

    def test_update_chunk_called_with_request_options(self):
        self.client.update_chunk = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        x.update(
            updates={"data": {"string_value": "This is an updated demo chunk."}},
            request_options=request_options,
        )

        self.client.update_chunk.assert_called_once_with(request, **request_options)

    def test_batch_update_chunks_called_with_request_options(self):
        self.client.batch_update_chunks = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        try:
            demo_corpus = retriever.create_corpus(name="demo-corpus")
            demo_document = demo_corpus.create_document(name="demo-doc")
            x = demo_document.create_chunk(
                name="demo-chunk",
                data="This is a demo chunk.",
            )
            y = demo_document.create_chunk(
                name="demo-chunk-1",
                data="This is another demo chunk.",
            )
            update_request = demo_document.batch_update_chunks(
                chunks=[
                    (
                        "corpora/demo-corpus/documents/demo-doc/chunks/demo-chunk",
                        {"data": {"string_value": "This is an updated chunk."}},
                    ),
                    (
                        "corpora/demo-corpus/documents/demo-doc/chunks/demo-chunk-1",
                        {"data": {"string_value": "This is another updated chunk."}},
                    ),
                ],
                request_options=request_options,
            )
        except AttributeError:
            pass

        self.client.batch_update_chunks.assert_called_once_with(request, **request_options)

    def test_delete_chunk_called_with_request_options(self):
        self.client.delete_chunk = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        delete_request = demo_document.delete_chunk(
            name="demo-chunk", request_options=request_options
        )

        self.client.delete_chunk.assert_called_once_with(request, **request_options)

    def test_batch_delete_chunks_called_with_request_options(self):
        self.client.batch_delete_chunks = unittest.mock.MagicMock()
        request = unittest.mock.ANY
        request_options = {"timeout": 120}

        demo_corpus = retriever.create_corpus(name="demo-corpus")
        demo_document = demo_corpus.create_document(name="demo-doc")
        x = demo_document.create_chunk(
            name="demo-chunk",
            data="This is a demo chunk.",
        )
        y = demo_document.create_chunk(
            name="demo-chunk",
            data="This is another demo chunk.",
        )
        delete_request = demo_document.batch_delete_chunks(
            chunks=[x.name, y.name], request_options=request_options
        )

        self.client.batch_delete_chunks.assert_called_once_with(request, **request_options)


if __name__ == "__main__":
    absltest.main()
