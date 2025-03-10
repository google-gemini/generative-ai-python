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

"""Tests for proxy configuration functionality."""

import os
import tempfile
import unittest
from unittest import mock
import pathlib
import socket
import threading
import time
import http.server
import socketserver
import json

import httplib2
import socks

import google.generativeai as genai
from google.generativeai.client import FileServiceClient, configure, _client_manager


class ProxyConfigUnitTest(unittest.TestCase):
    """Unit tests for proxy configuration."""

    def setUp(self):
        # Reset the client manager before each test
        _client_manager.clients = {}

    def test_proxy_info_passed_to_configure(self):
        """Test that proxy_info is stored in the client manager when configured."""
        proxy_info = httplib2.ProxyInfo(
            proxy_type=socks.PROXY_TYPE_HTTP,
            proxy_host='proxy-host',
            proxy_port=8080
        )
        
        configure(api_key="fake-key", proxy_info=proxy_info)
        
        # Verify proxy_info is stored in client manager
        self.assertEqual(_client_manager.proxy_info, proxy_info)

    def test_proxy_info_passed_to_file_service_client(self):
        """Test that proxy_info is passed to FileServiceClient."""
        proxy_info = httplib2.ProxyInfo(
            proxy_type=socks.PROXY_TYPE_HTTP,
            proxy_host='proxy-host',
            proxy_port=8080
        )
        
        http_mock = mock.MagicMock()
        http_mock.request.return_value = ({}, b'{"resources": {"media": {"methods": {"upload": {}}}}}')
        
        http_request_mock = mock.MagicMock()
        http_request_mock.execute.return_value = ({}, b'{"resources": {"media": {"methods": {"upload": {}}}}}')
        
        discovery_api_mock = mock.MagicMock()
        
        with mock.patch('httplib2.Http', return_value=http_mock) as http_class_mock, \
             mock.patch('googleapiclient.http.HttpRequest', return_value=http_request_mock), \
             mock.patch('googleapiclient.discovery.build_from_document', return_value=discovery_api_mock):
            
            # Configure with proxy_info
            configure(api_key="fake-key", proxy_info=proxy_info)
            
            # Create a file service client
            file_client = _client_manager.get_default_client("file")
            
            # Call _setup_discovery_api to trigger HTTP client creation
            file_client._setup_discovery_api()
            
            # Verify httplib2.Http was called with proxy_info
            http_class_mock.assert_called_with(proxy_info=proxy_info)

    def test_proxy_info_in_file_service_client_init(self):
        """Test that proxy_info is stored in the FileServiceClient instance."""
        proxy_info = httplib2.ProxyInfo(
            proxy_type=socks.PROXY_TYPE_HTTP,
            proxy_host='proxy-host',
            proxy_port=8080
        )
        
        # Create FileServiceClient directly with proxy_info
        with mock.patch('google.ai.generativelanguage.FileServiceClient.__init__', return_value=None):
            file_client = FileServiceClient(proxy_info=proxy_info)
            self.assertEqual(file_client._proxy_info, proxy_info)


class MockProxyServer(http.server.HTTPServer):
    """Mock proxy server for testing."""
    
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)
        self.requests = []


class MockProxyHandler(http.server.BaseHTTPRequestHandler):
    """Handler for mock proxy server."""
    
    def do_GET(self):
        """Handle GET requests."""
        self.server.requests.append({
            'path': self.path,
            'headers': dict(self.headers),
            'method': 'GET'
        })
        
        # Respond with success
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        # Send a mock discovery document
        response = {
            'version': 'v1beta',
            'name': 'generativelanguage',
            'title': 'Generative Language API',
            'description': 'Mock discovery document',
            'resources': {
                'media': {
                    'methods': {
                        'upload': {}
                    }
                }
            }
        }
        
        self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def do_POST(self):
        """Handle POST requests."""
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length else b''
        
        self.server.requests.append({
            'path': self.path,
            'headers': dict(self.headers),
            'method': 'POST',
            'body': body.decode('utf-8') if body else None
        })
        
        # Respond with success
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        
        # Send a mock file upload response
        response = {
            'file': {
                'name': 'files/test-file',
                'displayName': 'test-file.txt',
                'mimeType': 'text/plain',
            }
        }
        
        self.wfile.write(json.dumps(response).encode('utf-8'))
    
    def log_message(self, format, *args):
        """Suppress log messages to keep test output clean."""
        pass


@unittest.skip("Integration test requires network access - run manually")
class ProxyConfigIntegrationTest(unittest.TestCase):
    """Integration tests for proxy configuration.
    
    These tests require a real proxy server or a mock proxy server running.
    They are skipped by default and can be run manually.
    """
    
    def setUp(self):
        # Start a mock proxy server
        self.proxy_port = self._find_free_port()
        self.proxy_server = MockProxyServer(('localhost', self.proxy_port), MockProxyHandler)
        
        # Start the server in a separate thread
        self.server_thread = threading.Thread(target=self.proxy_server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()
        
        # Wait for server to start
        time.sleep(0.1)
        
        # Reset the client manager
        _client_manager.clients = {}
    
    def tearDown(self):
        # Shut down the proxy server
        if hasattr(self, 'proxy_server'):
            self.proxy_server.shutdown()
            self.proxy_server.server_close()
            self.server_thread.join(timeout=1)
    
    def _find_free_port(self):
        """Find a free port to use for the mock proxy server."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            return s.getsockname()[1]
    
    def test_file_upload_through_proxy(self):
        """Test that file uploads go through the proxy."""
        # Configure proxy
        proxy_info = httplib2.ProxyInfo(
            proxy_type=socks.PROXY_TYPE_HTTP,
            proxy_host='localhost',
            proxy_port=self.proxy_port
        )
        
        # Configure the API with mock API key and proxy
        genai.configure(api_key="fake-api-key", proxy_info=proxy_info)
        
        # Create a temporary file to upload
        with tempfile.NamedTemporaryFile(suffix='.txt') as temp_file:
            temp_file.write(b"Test content")
            temp_file.flush()
            
            # Override default discovery URL
            original_discovery_url = genai.client.GENAI_API_DISCOVERY_URL
            genai.client.GENAI_API_DISCOVERY_URL = f"http://localhost:{self.proxy_port}/discovery"
            
            try:
                # Patch socket module to route requests through our mock proxy
                with mock.patch('socket.socket'):
                    # Try to upload the file
                    file = genai.upload_file(path=temp_file.name)
                    
                    # Verify file was "uploaded" successfully
                    self.assertIsNotNone(file)
                    self.assertTrue(file.name.startswith('files/'))
                    
                    # Verify requests went through our mock proxy
                    self.assertGreaterEqual(len(self.proxy_server.requests), 1)
                    
                    # Verify the discovery request
                    discovery_request = None
                    for req in self.proxy_server.requests:
                        if '/discovery' in req['path']:
                            discovery_request = req
                            break
                    
                    self.assertIsNotNone(discovery_request)
                    self.assertEqual(discovery_request['method'], 'GET')
            finally:
                # Restore original discovery URL
                genai.client.GENAI_API_DISCOVERY_URL = original_discovery_url


if __name__ == '__main__':
    unittest.main() 