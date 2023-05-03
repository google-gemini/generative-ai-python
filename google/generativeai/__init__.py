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
"""A high level client library for generative AI.

## Setup

```
import google.generativeai as genai

genai.configure(api_key=os.environ['API_KEY']
```

## Chat

Use the `genai.chat` function to have a discussion with a model:

```
response = genai.chat(messages=["Hello."])
print(response.last) #  'Hello! What can I help you with?'
response.reply("Can you tell me a joke?")
```

## Models

Use the model service discover models and find out more about them:

Use `genai.get_model` to get details if you know a model's name:

```
model = genai.get_model('chat-bison-001') # 🦬
```

Use `genai.list_models` to discover models:

```
import pprint
for model in genai.list_models():
    pprint.pprint(model) # 🦎🦦🦬🦄
```

"""

from google.generativeai import types

from google.generativeai.discuss import chat
from google.generativeai.discuss import chat_async
from google.generativeai.discuss import count_message_tokens

from google.generativeai.text import generate_text
from google.generativeai.text import generate_embeddings

from google.generativeai.models import list_models
from google.generativeai.models import get_model


from google.generativeai.client import configure

del discuss
del text
del models
del client
