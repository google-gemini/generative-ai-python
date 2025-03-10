#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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
Example demonstrating how to use custom headers on a per-request basis with the Gemini API.
This is particularly useful when working with proxy services like Helicone, Traceloop, or LiteLLM.
"""

import os
import google.generativeai as genai
from google.generativeai.types import RequestOptions

# Configure the Gemini API with the provided API key
API_KEY = "AIzaSyBgUvB3zMMxGcjSJmMYVRD1ILiUcjxxAvQ"
genai.configure(api_key=API_KEY)

# Create a model
model = genai.GenerativeModel('gemini-1.5-flash')


def simple_example():
    """Example using simple standard HTTP headers."""
    print("\n=== Simple Headers Example ===")
    
    # Basic request without custom headers
    response1 = model.generate_content(
        'Tell me a joke about programming in one sentence.'
    )
    print(f"Response without headers: {response1.text}")
    
    # Request with custom headers
    response2 = model.generate_content(
        'Tell me a joke about cats in one sentence.',
        request_options=RequestOptions(
            extra_headers=[
                ('x-custom-user-id', 'user123'),
                ('x-custom-session', 'session456')
            ]
        )
    )
    print(f"Response with custom headers: {response2.text}")


def custom_headers_example():
    """Example using custom headers."""
    print("\n=== Custom Headers Example ===")
    
    response = model.generate_content(
        'Explain the concept of machine learning in one sentence.',
        request_options=RequestOptions(
            extra_headers=[
                ('x-tracking-id', 'track789'),
                ('x-client-version', '1.0.0')
            ]
        )
    )
    print(f"Response with tracking headers: {response.text}")


def multiple_requests_example():
    """Example demonstrating multiple requests with different headers."""
    print("\n=== Multiple Requests Example ===")
    
    # First request with one set of headers
    print("Request 1:")
    response1 = model.generate_content(
        'What is the capital of France?',
        request_options=RequestOptions(
            extra_headers=[
                ('x-request-id', 'req1'),
                ('x-user-id', 'user-a')
            ]
        )
    )
    print(f"Response: {response1.text}")
    
    # Second request with different headers
    print("\nRequest 2:")
    response2 = model.generate_content(
        'What is the capital of Italy?',
        request_options=RequestOptions(
            extra_headers=[
                ('x-request-id', 'req2'),
                ('x-user-id', 'user-b')
            ]
        )
    )
    print(f"Response: {response2.text}")
    
    # Third request with no headers
    print("\nRequest 3 (no custom headers):")
    response3 = model.generate_content(
        'What is the capital of Germany?'
    )
    print(f"Response: {response3.text}")


def timeout_example():
    """Example with timeout in RequestOptions along with headers."""
    print("\n=== Timeout with Headers Example ===")
    
    response = model.generate_content(
        'Write a haiku about coding.',
        request_options=RequestOptions(
            timeout=30,  # 30 seconds timeout
            extra_headers=[
                ('x-request-source', 'example-script'),
                ('x-request-type', 'haiku')
            ]
        )
    )
    print(f"Response with timeout and headers: {response.text}")


def count_tokens_example():
    """Example showing custom headers with count_tokens."""
    print("\n=== Count Tokens with Headers Example ===")
    
    # Count tokens without custom headers
    content = "This is a test sentence to count tokens. It should have more than a few tokens."
    token_count1 = model.count_tokens(content)
    print(f"Token count without headers: {token_count1.total_tokens}")
    
    # Count tokens with custom headers
    token_count2 = model.count_tokens(
        content,
        request_options=RequestOptions(
            extra_headers=[
                ('x-token-count-request-id', 'count123'),
                ('x-analytics-source', 'example-script')
            ]
        )
    )
    print(f"Token count with headers: {token_count2.total_tokens}")
    
    # The token counts should be the same, showing that the headers don't affect the functionality
    print(f"Token counts match: {token_count1.total_tokens == token_count2.total_tokens}")


def main():
    print("=== Per-Request Headers Examples ===")
    print("Demonstrating how to use custom headers on a per-request basis")
    
    # Run examples
    simple_example()
    custom_headers_example()
    multiple_requests_example()
    timeout_example()
    count_tokens_example()


if __name__ == "__main__":
    main() 