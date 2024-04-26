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

import google.api_core.timeout
import google.api_core.retry

import dataclasses

from typing_extensions import TypedDict, Union


class RequestOptionsDict(TypedDict, total=False):
    retry: google.api_core.retry.Retry
    timeout: int | float | google.api_core.timeout.TimeToDeadlineTimeout


@dataclasses.dataclass
class RequestOptions:
    retry: google.api_core.retry.Retry | None
    timeout: int | float | google.api_core.timeout.TimeToDeadlineTimeout | None

    def to_dict(self):
        result = {}

        retry = self.retry
        if retry is not None:
            result["retry"] = retry
        timeout = self.timeout
        if timeout is not None:
            result["timeout"] = timeout

        return result


RequestOptionsType = Union[RequestOptions, RequestOptionsDict]


def echo(request_options):
    if isinstance(request_options, RequestOptions):
        return request_options.to_dict()
    elif isinstance(request_options, dict):
        return request_options
