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
"""
This module publishes the proto classes from `google.ai.generativelanguage`.

`google.ai.generativelanguage` is a low-level auto-generated client library for the Gemini API.

It is built using the same tooling as Google Cloud client libraries, and will be quite familiar if you've used
those before.

While we encourage Python users to access the Geini API using the `google.generativeai` package (aka `palm`),
the lower level package is also available.

Each method in the Gemini API is connected to one of the client classes. Pass your API-key to the class' `client_options`
when initializing a client:

```
from google.generativeai import protos

client = protos.DiscussServiceClient(
    client_options={'api_key':'YOUR_API_KEY'})
```

To call the api, pass an appropriate request-proto-object. For the `DiscussServiceClient.generate_message` pass
a `generativelanguage.GenerateMessageRequest` instance:

```
request = protos.GenerateMessageRequest(
    model='models/chat-bison-001',
    prompt=protos.MessagePrompt(
        messages=[protos.Message(content='Hello!')]))

client.generate_message(request)
```
```
candidates {
  author: "1"
  content: "Hello! How can I help you today?"
}
...
```

For simplicity:

* The API methods also accept key-word arguments.
* Anywhere you might pass a proto-object, the library will also accept simple python structures.

So the following is equivalent to the previous example:

```
client.generate_message(
    model='models/chat-bison-001',
    prompt={'messages':[{'content':'Hello!'}]})
```
```
candidates {
  author: "1"
  content: "Hello! How can I help you today?"
}
...
```

"""

from google.ai.generativelanguage_v1beta.types import *
from google.ai.generativelanguage_v1beta.types import __all__
