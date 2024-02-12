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
import unittest
import unittest.mock as mock

import google.ai.generativelanguage as glm

from google.generativeai import retriever
from google.generativeai import permission
from google.generativeai.types import permission_types as permission_services
from google.generativeai.types import retriever_types as retriever_services

from google.generativeai import client
from absl.testing import absltest
from absl.testing import parameterized


class AsyncTests(parameterized.TestCase, unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = unittest.mock.AsyncMock()

        client._client_manager.clients["retriever_async"] = self.client
        client._client_manager.clients["permission_async"] = self.client

        self.observed_requests = []

        self.responses = {}

        def add_client_method(f):
            name = f.__name__
            setattr(self.client, name, f)
            return f

        @add_client_method
        async def create_corpus(
            request: glm.CreateCorpusRequest,
        ) -> glm.Corpus:
            self.observed_requests.append(request)
            return glm.Corpus(
                name="corpora/demo_corpus",
                display_name="demo-corpus",
                create_time="2000-01-01T01:01:01.123456Z",
                update_time="2000-01-01T01:01:01.123456Z",
            )
        
        @add_client_method
        async def create_permission(
            request: glm.CreatePermissionRequest,
        ) -> glm.Permission:
            self.observed_requests.append(request)
            return glm.Permission(
                name="corpora/demo_corpus/permissions/123456789",
                role=2,
                grantee_type=3,
            )
    
        @add_client_method
        async def delete_permission(
            request: glm.DeletePermissionRequest,
        ) -> None:
            self.observed_requests.append(request)
            return None
        
        @add_client_method
        async def get_permission(
            request: glm.GetPermissionRequest,
        ) -> glm.Permission:
            self.observed_requests.append(request)
            return glm.Permission(
                name="corpora/demo_corpus/permissions/123456789",
                role=2,
                grantee_type=3,
            )

        @add_client_method
        async def list_permissions(
            request: glm.ListPermissionsRequest,
        ) -> glm.ListPermissionsResponse:
            self.observed_requests.append(request)
            async def results():
                yield glm.Permission(
                    name="corpora/demo_corpus/permissions/123456789",
                    role=2,
                    grantee_type=3,
                )
                yield glm.Permission(
                    name="corpora/demo_corpus/permissions/987654321",
                    role=3,
                    grantee_type=3,
                    email_address="_"
                )

            return results()
        
        @add_client_method
        async def update_permission(
            request: glm.UpdatePermissionRequest,
        ) -> glm.Permission:
            self.observed_requests.append(request)
            return glm.Permission(
                name="corpora/demo_corpus/permissions/123456789",
                role=3,
                grantee_type=3,
            )
    @parameterized.named_parameters(
        [
            dict(
                testcase_name="create_permission_success",
                role=2,
                grantee_type=3,
                email_address=None
            ),
            dict(
                testcase_name="create_permission_failure_email_set_when_grantee_type_is_everyone",
                role=2,
                grantee_type=3,
                email_address="_"
            ),
            dict(
                testcase_name="create_permission_failure_email_not_set_when_grantee_type_is_not_everyone",
                role=2,
                grantee_type=1,
                email_address=None
            ),
        ]
    )
    async def test_create_permission(self, role, grantee_type, email_address):
        x = await retriever.create_corpus_async("demo-corpus")
        if (role, grantee_type, email_address) == (2, 3, None):
            perm = await x.create_permission_async(
                role=role,
                grantee_type=grantee_type,
                email_address=email_address
            )
            self.assertIsInstance(perm, permission_services.Permission)
            self.assertIsInstance(self.observed_requests[-1], glm.CreatePermissionRequest)

        elif (role, grantee_type, email_address) == (2, 3, ""):
            with self.assertRaises(ValueError):
                perm = await x.create_permission_async(
                    role=role,
                    grantee_type=grantee_type,
                    email_address=email_address
                )            
        
        elif (role, grantee_type, email_address) == (2, 1, None):
            with self.assertRaises(ValueError):
                perm = await x.create_permission_async(
                    role=role,
                    grantee_type=grantee_type,
                    email_address=email_address
                )        
    
    async def test_delete_permission(self):
        x = await retriever.create_corpus_async("demo-corpus")
        perm = await x.create_permission_async(2, 3)
        await perm.delete_async()
        self.assertIsInstance(self.observed_requests[-1], glm.DeletePermissionRequest)
    
    async def test_get_permission(self):
        x = await retriever.create_corpus_async("demo-corpus")
        perm = await x.create_permission_async(2, 3)
        fetch_perm = await permission.get_permission_async(name=perm.name)
        self.assertIsInstance(fetch_perm, permission_services.Permission)
        self.assertIsInstance(self.observed_requests[-1], glm.GetPermissionRequest)
        self.assertEqual(fetch_perm, perm)
    
    async def test_list_permission(self):
        x = await retriever.create_corpus_async("demo-corpus")
        perm1 = await x.create_permission_async(2, 3)
        perm2 = await x.create_permission_async(3, 2, "_")
        perms = [perm async for perm in x.list_permissions_async(page_size=1)]
        self.assertEqual(len(perms), 2)
        self.assertEqual(perm1, perms[0])
        self.assertEqual(perms[1].email_address, "_")
        for perm in perms:
            self.assertIsInstance(perm, permission_services.Permission)
        self.assertIsInstance(self.observed_requests[-1], glm.ListPermissionsRequest)
    
    @parameterized.named_parameters(
        [
            dict(
                testcase_name="update_permission_success",
                updates={"role": 2}
            )
        ]
    )
    async def test_update_permission(self, updates):
        x = await retriever.create_corpus_async("demo-corpus")
        perm = await x.create_permission_async(2, 3)
        updated_perm = await perm.update_async(updates=updates)
        self.assertIsInstance(updated_perm, permission_services.Permission)
        self.assertIsInstance(self.observed_requests[-1], glm.UpdatePermissionRequest)


if __name__ == "__main__":
    absltest.main()
