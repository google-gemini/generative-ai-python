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
from __future__ import annotations

from typing import Iterator
from google.ai import generativelanguage as glm
from google.generativeai.types import model_types
from google.api_core import operation as operations
from google.api_core import protobuf_helpers


class CreateTunedModelOperation(operations.Operation):

    @staticmethod
    def from_core_operation(
        operation: operations.Operation,
    ) -> CreateTunedModelOperation:
        polling = getattr(operation, "_polling", None)
        retry = getattr(operation, "_retry", None)
        if polling is not None:
            # google.api_core v 2.11
            kwargs = {"polling": polling}
        elif retry is not None:
            # google.api_core v 2.10
            kwargs = {"retry": retry}
        else:
            kwargs = {}
        return CreateTunedModelOperation(
            operation=operation._operation,
            refresh=operation._refresh,
            cancel=operation._cancel,
            result_type=operation._result_type,
            metadata_type=operation._metadata_type,
            **kwargs,
        )

    def update(self):
        """Refresh the current statuses in metadata/result/error"""
        self._refresh_and_update()

    def wait_bar(self, **kwargs) -> Iterator[glm.CreateTunedModelMetadata]:
        """A tqdm wait bar, yields `Operation` statuses until complete.

        Args:
            **kwargs: passed through to `tqdm.auto.tqdm(..., **kwargs)`

        Yields:
            Operation statuses as `glm.CreateTunedModelMetadata` objects.
        """
        import tqdm.auto as tqdm

        bar = tqdm.tqdm(total=self.metadata.total_steps, initial=0, **kwargs)

        # done() includes a `_refresh_and_update`
        while not self.done():
            metadata = self.metadata
            bar.update(self.metadata.completed_steps - bar.n)
            yield metadata
        metadata = self.metadata
        bar.update(self.metadata.completed_steps - bar.n)

    @property
    def _operation(self):
        # Workaround for b/297095680.
        return self.__dict__['_operation']

    @_operation.setter
    def _operation(self, op):
        # Workaround for b/297095680.
        op.response.type_url = op.response.type_url.replace("v1main", "v1beta3")
        op.metadata.type_url = op.metadata.type_url.replace("v1main", "v1beta3")
        self.__dict__['_operation'] = op

    def set_result(self, result: glm.TunedModel):
        result = model_types.decode_tuned_model(result)
        super().set_result(result)
