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

from contextlib import redirect_stderr
import io

from google.generativeai import protos
import google.protobuf.any_pb2

import google.generativeai.operations as genai_operation
from google.generativeai.types import model_types
import google.api_core.operation as core_operation

from absl.testing import absltest
from absl.testing import parameterized


class OperationsTests(parameterized.TestCase):
    metadata_type = (
        "type.googleapis.com/google.ai.generativelanguage.v1beta.CreateTunedModelMetadata"
    )
    result_type = "type.googleapis.com/google.ai.generativelanguage.v1beta.TunedModel"

    def test_end_to_end(self):
        name = "my-model"

        # Operation is defined here: https://github.com/googleapis/googleapis/blob/master/google/longrunning/operations.proto#L128
        # It uses `google.protobuf.Any` to encode the metadata and results
        # `Any` takes a type name and a serialized proto.
        metadata = google.protobuf.any_pb2.Any(
            type_url=self.metadata_type,
            value=protos.CreateTunedModelMetadata(tuned_model=name)._pb.SerializeToString(),
        )

        # Initially the `Operation` is not `done`, so it only gives a metadata.
        initial_pb = core_operation.operations_pb2.Operation(
            name=f"tunedModels/{name}/operations/urvodfipaft0",
            done=False,
            metadata=metadata,
        )

        # When the `Operation` is `done`, it returns a `response`
        final_pb = core_operation.operations_pb2.Operation(
            name=f"tunedModels/{name}/operations/urvodfipaft0",
            done=True,
            metadata=metadata,
            response=google.protobuf.any_pb2.Any(
                type_url=self.result_type,
                value=protos.TunedModel(name=name)._pb.SerializeToString(),
            ),
        )

        # Create the operation with the `initial_pb` but when it asks for an update
        # return the `final_pb`.
        def refresh(*_, **__):
            return final_pb

        # This is the base Operation class
        operation = core_operation.Operation(
            operation=initial_pb,
            refresh=refresh,
            cancel=lambda: print(f"cancel!"),
            result_type=protos.TunedModel,
            metadata_type=protos.CreateTunedModelMetadata,
        )

        # Use our wrapper instead.
        ctm_op = genai_operation.CreateTunedModelOperation.from_core_operation(operation)

        # Test that the metadata was decoded
        meta = ctm_op.metadata
        self.assertEqual(meta.tuned_model, name)

        # Update the status to get the `final_pb`
        result = ctm_op.result()

        # Check that the result was decoded.
        self.assertIsInstance(result, model_types.TunedModel)
        self.assertEqual(result.name, name)

    def test_wait_bar(self):
        name = "my-model"

        def gen_operations():
            """yield 10+done incremental operation statuses"""

            def make_metadata(completed_steps):
                return google.protobuf.any_pb2.Any(
                    type_url=self.metadata_type,
                    value=protos.CreateTunedModelMetadata(
                        tuned_model=name,
                        total_steps=total_steps,
                        completed_steps=completed_steps,
                    )._pb.SerializeToString(),
                )

            total_steps = 10
            for completed_steps in range(total_steps):
                metadata = make_metadata(completed_steps)

                yield core_operation.operations_pb2.Operation(
                    name=f"tunedModels/{name}/operations/urvodfipaft0",
                    done=False,
                    metadata=metadata,
                )

            op = core_operation.operations_pb2.Operation(
                name=f"tunedModels/{name}/operations/urvodfipaft0",
                done=True,
                metadata=make_metadata(total_steps),
                response=google.protobuf.any_pb2.Any(
                    type_url=self.result_type,
                    value=protos.TunedModel(name=name)._pb.SerializeToString(),
                ),
            )

            while True:
                yield op

        # pop the initial status
        ops = gen_operations()
        initial_pb = next(ops)

        def refresh(*_, **__):
            """get the next status on each refresh"""
            return next(ops)

        # This is the base Operation class
        operation = core_operation.Operation(
            operation=initial_pb,
            refresh=refresh,
            cancel=None,
            result_type=protos.TunedModel,
            metadata_type=protos.CreateTunedModelMetadata,
        )

        # Use our wrapper instead.
        ctm_op = genai_operation.CreateTunedModelOperation.from_core_operation(operation)

        # Capture the stderr so we can check the wait-bar.
        f = io.StringIO()
        with redirect_stderr(f):
            for status in ctm_op.wait_bar():
                pass

        s = f.getvalue()
        self.assertIn("100%|##########| 10/10", s)
        self.assertTrue(ctm_op.done())


if __name__ == "__main__":
    absltest.main()
