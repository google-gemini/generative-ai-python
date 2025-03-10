#!/usr/bin/env python
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

"""
Demonstration script for using the Google Generative AI SDK with a proxy.

This script shows how to configure the SDK to use a proxy for all API calls,
including file uploads. It includes examples of basic text generation and
working with images through a proxy.

Usage:
    python proxy_demo.py

Requirements:
    - google-generativeai
    - httplib2
    - PySocks
    - PIL (for image example)
"""

import os
import argparse
import tempfile
import pathlib

import httplib2
import socks
try:
    from PIL import Image
except ImportError:
    Image = None

import google.generativeai as genai


def create_proxy_info(host, port, user=None, password=None):
    """Create a ProxyInfo object for the given proxy configuration."""
    print(f"Configuring proxy: {host}:{port}")
    if user and password:
        print(f"Using authenticated proxy with user: {user}")
        return httplib2.ProxyInfo(
            proxy_type=socks.PROXY_TYPE_HTTP,
            proxy_host=host,
            proxy_port=port,
            proxy_user=user,
            proxy_pass=password
        )
    else:
        print("Using unauthenticated proxy")
        return httplib2.ProxyInfo(
            proxy_type=socks.PROXY_TYPE_HTTP,
            proxy_host=host,
            proxy_port=port
        )


def text_generation_example(api_key):
    """Run a basic text generation example."""
    print("\n=== Basic Text Generation Example ===")
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = "What are the top 5 considerations when implementing a proxy server for API traffic?"
    print(f"Prompt: {prompt}")
    
    try:
        response = model.generate_content(prompt)
        print("\nResponse:")
        print(response.text)
        return True
    except Exception as e:
        print(f"Error generating content: {e}")
        return False


def file_upload_example(api_key):
    """Run a file upload example."""
    print("\n=== File Upload Example ===")
    
    # Create a temporary text file
    with tempfile.NamedTemporaryFile(suffix='.txt', delete=False) as temp_file:
        temp_path = temp_file.name
        content = """
        # Proxy Configuration Best Practices
        
        1. Security: Always use TLS for encrypted connections
        2. Authentication: Implement proper access controls
        3. Logging: Maintain detailed logs for troubleshooting
        4. Performance: Consider caching mechanisms
        5. Scalability: Design for increasing loads
        """
        temp_file.write(content.encode('utf-8'))
    
    try:
        print(f"Uploading temporary file: {temp_path}")
        file = genai.upload_file(path=temp_path)
        print(f"File uploaded successfully with name: {file.name}")
        
        # Use the file in a generation request
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Summarize this document in three bullet points:"
        
        print(f"Prompt: {prompt}")
        response = model.generate_content([prompt, file])
        
        print("\nResponse:")
        print(response.text)
        
        # Clean up
        os.unlink(temp_path)
        genai.delete_file(file.name)
        return True
    except Exception as e:
        print(f"Error in file upload example: {e}")
        # Clean up
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        return False


def image_example(api_key):
    """Run an example with image input."""
    if not Image:
        print("\n=== Image Example Skipped (PIL not installed) ===")
        return False
    
    print("\n=== Image Example ===")
    
    # Create a simple test image
    width, height = 200, 200
    img = Image.new('RGB', (width, height), color='red')
    
    # Add a blue square in the center
    center_size = 100
    offset = (width - center_size) // 2
    blue_square = Image.new('RGB', (center_size, center_size), color='blue')
    img.paste(blue_square, (offset, offset))
    
    # Save the image to a temporary file
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
        temp_path = temp_file.name
        img.save(temp_path)
    
    try:
        # Use the image in a generation request
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = "Describe this image in detail:"
        
        print(f"Prompt: {prompt}")
        response = model.generate_content([prompt, Image.open(temp_path)])
        
        print("\nResponse:")
        print(response.text)
        
        # Clean up
        os.unlink(temp_path)
        return True
    except Exception as e:
        print(f"Error in image example: {e}")
        # Clean up
        if os.path.exists(temp_path):
            os.unlink(temp_path)
        return False


def main():
    """Run the proxy demo with command line arguments."""
    parser = argparse.ArgumentParser(description='Demonstrate Google Generative AI SDK with proxy support')
    parser.add_argument('--api-key', help='Gemini API key (or set GEMINI_API_KEY environment variable)')
    parser.add_argument('--proxy-host', required=True, help='Proxy server hostname or IP')
    parser.add_argument('--proxy-port', type=int, required=True, help='Proxy server port')
    parser.add_argument('--proxy-user', help='Proxy username (for authenticated proxies)')
    parser.add_argument('--proxy-password', help='Proxy password (for authenticated proxies)')
    parser.add_argument('--skip-file-upload', action='store_true', help='Skip file upload example')
    parser.add_argument('--skip-image', action='store_true', help='Skip image example')
    
    args = parser.parse_args()
    
    # Get API key from command line or environment
    api_key = args.api_key or os.environ.get('GEMINI_API_KEY')
    if not api_key:
        print("Error: API key is required. Provide --api-key or set GEMINI_API_KEY environment variable.")
        return 1
    
    # Create proxy configuration
    proxy_info = create_proxy_info(
        host=args.proxy_host,
        port=args.proxy_port,
        user=args.proxy_user,
        password=args.proxy_password
    )
    
    # Configure the SDK with proxy
    print(f"Configuring Gemini API with proxy")
    genai.configure(api_key=api_key, proxy_info=proxy_info)
    
    # Run examples
    success = text_generation_example(api_key)
    
    if success and not args.skip_file_upload:
        file_success = file_upload_example(api_key)
        if not file_success:
            print("File upload example failed. This may be due to proxy restrictions.")
    
    if success and not args.skip_image and Image:
        image_success = image_example(api_key)
        if not image_success:
            print("Image example failed. This may be due to proxy restrictions.")
    
    print("\nDemo completed.")
    return 0


if __name__ == "__main__":
    exit(main()) 