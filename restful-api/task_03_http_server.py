#!/usr/bin/python3
"""Custom HTTP request handler class to handle GET requests."""


import http.server
import json
import socketserver

PORT = 8000


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests based on the request path."""

        print("Received GET request for path: {}".format(self.path))

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            response = "Hello, this is a simple API!"
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            response = json.dumps(data)
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            status = {"status": "OK"}
            response = json.dumps(status)
            self.wfile.write(response.encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            response = json.dumps(info)
            self.wfile.write(response.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            error = {"error": "Endpoint not found"}
            response = json.dumps(error)
            self.wfile.write(response.encode('utf-8'))


"""Server configuration and startup"""
if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print("Serving on port {}".format(PORT))
        httpd.serve_forever()
