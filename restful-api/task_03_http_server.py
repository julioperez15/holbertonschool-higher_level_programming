#!/usr/bin/python3


import http.server
import socketserver
import json


class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(bytes(json.dumps(data), "utf8"))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes("OK", "utf8"))
        elif self.path == '/info':
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0", "description":
                "A simple API built with http.server"}
            self.wfile.write(bytes(json.dumps(info), "utf8"))
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", "utf8"))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("404 Not Found", "utf8"))


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, MyHttpRequestHandler)
    httpd.serve_forever()
