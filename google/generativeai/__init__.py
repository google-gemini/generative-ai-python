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
"""Google AI Python SDK

## Setup

```posix-terminal
pip install google-generativeai
```

## GenerativeModel

Use `genai.GenerativeModel` to access the API:

```
import google.generativeai as genai
import os

genai.configure(api_key=os.environ['API_KEY'])

model = genai.GenerativeModel(model_name='gemini-1.5-flash')
response = model.generate_content('Teach me about how an LLM works')

print(response.text)
```

See the [python quickstart](https://ai.google.dev/tutorials/python_quickstart) for more details.
"""
# Main initialization file for Google's Generative AI SDK
# This file serves as the primary entry point for the SDK

# Future imports for Python 2/3 compatibility
from __future__ import annotations

# Import core version information
from google.generativeai import version

# Import key functionality modules
from google.generativeai import caching      # Handles caching of API responses
from google.generativeai import protos       # Protocol buffers for API communication
from google.generativeai import types        # Type definitions and hints

# Import core client configuration
from google.generativeai.client import configure  # Handles API authentication and setup

# Import embedding-related functions
from google.generativeai.embedding import (
    embed_content,           # Synchronous content embedding
    embed_content_async      # Asynchronous content embedding
)

# Import file management functions
from google.generativeai.files import (
    upload_file,            # Upload files to the API
    get_file,              # Retrieve file information
    list_files,            # List available files
    delete_file            # Remove files from the API
)

# Import core generative AI functionality
from google.generativeai.generative_models import (
    GenerativeModel,        # Main class for text generation
    ChatSession            # Handles conversational interactions
)

# Import model management functions
from google.generativeai.models import (
    list_models,           # List available base models
    list_tuned_models,     # List custom-tuned models
    get_model,             # Get specific model information
    get_base_model,        # Get base model details
    get_tuned_model,       # Get tuned model details
    create_tuned_model,    # Create a new tuned model
    update_tuned_model,    # Update existing tuned model
    delete_tuned_model     # Remove tuned model
)

# Import operation management functions
from google.generativeai.operations import (
    list_operations,       # List ongoing operations
    get_operation          # Get specific operation details
)

# Import configuration types
from google.generativeai.types import GenerationConfig  # Configuration for text generation

# Set version number from imported version file
__version__ = version.__version__

# Clean up namespace by removing imported modules
# This prevents them from being directly accessible
del embedding
del files
del generative_models
del models
del client
del operations
del version
