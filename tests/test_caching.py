# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
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
import datetime
import textwrap
import unittest

from google.generativeai import caching
from google.generativeai import protos

from google.generativeai import client
from absl.testing import absltest
from absl.testing import parameterized


class UnitTests(parameterized.TestCase):
    def setUp(self):
        self.client = unittest.mock.MagicMock()

        client._client_manager.clients["cache"] = self.client

        self.observed_requests = []

        def add_client_method(f):
            name = f.__name__
            setattr(self.client, name, f)
            return f

        @add_client_method
        def create_cached_content(
            request: protos.CreateCachedContentRequest,
            **kwargs,
        ) -> protos.CachedContent:
            self.observed_requests.append(request)
            return protos.CachedContent(
                name="cachedContents/test-cached-content",
                model="models/gemini-1.5-pro",
                display_name="Cached content for test",
                usage_metadata={"total_token_count": 1},
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
                expire_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def get_cached_content(
            request: protos.GetCachedContentRequest,
            **kwargs,
        ) -> protos.CachedContent:
            self.observed_requests.append(request)
            return protos.CachedContent(
                name="cachedContents/test-cached-content",
                model="models/gemini-1.5-pro",
                display_name="Cached content for test",
                usage_metadata={"total_token_count": 1},
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
                expire_time="2000-01-01T01:01:01.123456Z",
            )

        @add_client_method
        def list_cached_contents(
            request: protos.ListCachedContentsRequest,
            **kwargs,
        ) -> protos.ListCachedContentsResponse:
            self.observed_requests.append(request)
            return [
                protos.CachedContent(
                    name="cachedContents/test-cached-content-1",
                    model="models/gemini-1.5-pro",
                    display_name="Cached content for test",
                    usage_metadata={"total_token_count": 1},
                    create_time="2000-01-01T01:01:01.123456Z",
                    update_time="2000-01-01T01:01:01.123456Z",
                    expire_time="2000-01-01T01:01:01.123456Z",
                ),
                protos.CachedContent(
                    name="cachedContents/test-cached-content-2",
                    model="models/gemini-1.5-pro",
                    display_name="Cached content for test",
                    usage_metadata={"total_token_count": 1},
                    create_time="2000-01-01T01:01:01.123456Z",
                    update_time="2000-01-01T01:01:01.123456Z",
                    expire_time="2000-01-01T01:01:01.123456Z",
                ),
            ]

        @add_client_method
        def update_cached_content(
            request: protos.UpdateCachedContentRequest,
            **kwargs,
        ) -> protos.CachedContent:
            self.observed_requests.append(request)
            return protos.CachedContent(
                name="cachedContents/test-cached-content",
                model="models/gemini-1.5-pro",
                display_name="Cached content for test",
                usage_metadata={"total_token_count": 1},
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
                expire_time="2000-01-01T03:01:01.123456Z",
            )

        @add_client_method
        def delete_cached_content(
            request: protos.DeleteCachedContentRequest,
            **kwargs,
        ) -> None:
            self.observed_requests.append(request)

    def test_create_cached_content(self):

        def add(a: int, b: int) -> int:
            return a + b

        cc = caching.CachedContent.create(
            model="models/gemini-1.5-pro",
            contents=["Add 5 and 6"],
            tools=[add],
            tool_config={"function_calling_config": "ANY"},
            system_instruction="Always add 10 to the result.",
            ttl=datetime.timedelta(minutes=30),
        )
        self.assertIsInstance(self.observed_requests[-1], protos.CreateCachedContentRequest)
        self.assertIsInstance(cc, caching.CachedContent)
        self.assertEqual(cc.name, "cachedContents/test-cached-content")
        self.assertEqual(cc.model, "models/gemini-1.5-pro")

    @parameterized.named_parameters(
        [
            dict(
                testcase_name="ttl-is-int-seconds",
                ttl=7200,
            ),
            dict(
                testcase_name="ttl-is-timedelta",
                ttl=datetime.timedelta(hours=2),
            ),
            dict(
                testcase_name="ttl-is-dict",
                ttl={"seconds": 7200},
            ),
            dict(
                testcase_name="ttl-is-none-default-to-1-hr",
                ttl=None,
            ),
        ]
    )
    def test_ttl_types_for_create_cached_content(self, ttl):
        cc = caching.CachedContent.create(
            model="models/gemini-1.5-pro",
            contents=["cache this please for 2 hours"],
            ttl=ttl,
        )
        self.assertIsInstance(self.observed_requests[-1], protos.CreateCachedContentRequest)
        self.assertIsInstance(cc, caching.CachedContent)

    @parameterized.named_parameters(
        [
            dict(
                testcase_name="expire_time-is-int-seconds",
                expire_time=1717653421,
            ),
            dict(
                testcase_name="expire_time-is-datetime",
                expire_time=datetime.datetime.now(),
            ),
            dict(
                testcase_name="expire_time-is-dict",
                expire_time={"seconds": 1717653421},
            ),
            dict(
                testcase_name="expire_time-is-none-default-to-1-hr",
                expire_time=None,
            ),
        ]
    )
    def test_expire_time_types_for_create_cached_content(self, expire_time):
        cc = caching.CachedContent.create(
            model="models/gemini-1.5-pro",
            contents=["cache this please for 2 hours"],
            expire_time=expire_time,
        )
        self.assertIsInstance(self.observed_requests[-1], protos.CreateCachedContentRequest)
        self.assertIsInstance(cc, caching.CachedContent)

    def test_mutual_exclusivity_for_ttl_and_expire_time_in_create_cached_content(self):
        with self.assertRaises(ValueError):
            _ = caching.CachedContent.create(
                model="models/gemini-1.5-pro",
                contents=["cache this please for 2 hours"],
                ttl=datetime.timedelta(hours=2),
                expire_time=datetime.datetime.now(),
            )

    def test_get_cached_content(self):
        cc = caching.CachedContent.get(name="cachedContents/test-cached-content")
        self.assertIsInstance(self.observed_requests[-1], protos.GetCachedContentRequest)
        self.assertIsInstance(cc, caching.CachedContent)
        self.assertEqual(cc.name, "cachedContents/test-cached-content")
        self.assertEqual(cc.model, "models/gemini-1.5-pro")

    def test_list_cached_contents(self):
        ccs = list(caching.CachedContent.list(page_size=2))
        self.assertIsInstance(self.observed_requests[-1], protos.ListCachedContentsRequest)
        self.assertLen(ccs, 2)
        self.assertIsInstance(ccs[0], caching.CachedContent)
        self.assertIsInstance(ccs[1], caching.CachedContent)

    def test_update_cached_content_ttl_and_expire_time_are_mutually_exclusive(self):
        ttl = datetime.timedelta(hours=2)
        expire_time = datetime.datetime.now()

        cc = caching.CachedContent.get(name="cachedContents/test-cached-content")
        with self.assertRaises(ValueError):
            cc.update(ttl=ttl, expire_time=expire_time)

    @parameterized.named_parameters(
        [
            dict(testcase_name="ttl", ttl=datetime.timedelta(hours=2)),
            dict(
                testcase_name="expire_time",
                expire_time=datetime.datetime(2024, 6, 5, 12, 12, 12, 23),
            ),
        ]
    )
    def test_update_cached_content_valid_update_paths(self, ttl=None, expire_time=None):

        cc = caching.CachedContent.get(name="cachedContents/test-cached-content")
        cc.update(ttl=ttl, expire_time=expire_time)
        self.assertIsInstance(self.observed_requests[-1], protos.UpdateCachedContentRequest)
        self.assertIsInstance(cc, caching.CachedContent)

    def test_delete_cached_content(self):
        cc = caching.CachedContent.get(name="cachedContents/test-cached-content")
        cc.delete()
        self.assertIsInstance(self.observed_requests[-1], protos.DeleteCachedContentRequest)

        cc = caching.CachedContent.get(name="cachedContents/test-cached-content")
        cc.delete()
        self.assertIsInstance(self.observed_requests[-1], protos.DeleteCachedContentRequest)

    def test_repr_cached_content(self):
        expexted_repr = textwrap.dedent(
            """\
            CachedContent(
                name='cachedContents/test-cached-content',
                model='models/gemini-1.5-pro',
                display_name='Cached content for test',
                usage_metadata={
                    'total_token_count': 1,
                },
                create_time=2000-01-01 01:01:01.123456+00:00,
                update_time=2000-01-01 01:01:01.123456+00:00,
                expire_time=2000-01-01 01:01:01.123456+00:00
            )"""
        )
        cc = caching.CachedContent.get(name="cachedContents/test-cached-content")
        self.assertEqual(repr(cc), expexted_repr)


if __name__ == "__main__":
    absltest.main()
