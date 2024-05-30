#!/usr/bin/python3
"""A simple HTTP request handler to serve different endpoints."""
import http.server
import socketserver
import json

PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    """Custom HTTP request handler class to handle GET requests."""

    def do_GET(self):
        """Handle GET requests based on the request path."""
        if self.path == "/":
            # Respond with a plain text message
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode('utf-8'))
        elif self.path == "/data":
            # Respond with a JSON object
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        elif self.path == "/status":
            # Respond with a JSON status
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "OK"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        elif self.path == "/info":
            # Respond with a JSON info
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"version": "1.0",
                        "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            # Respond with a 404 error for undefined endpoints
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(response).encode('utf-8'))


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    """Start the server on the specified port and handle requests."""
    print("Serving at port {}".format(PORT))
    httpd.serve_forever()
