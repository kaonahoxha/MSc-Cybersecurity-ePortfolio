import os
from http.server import BaseHTTPRequestHandler, HTTPServer

class App(BaseHTTPRequestHandler):
    def do_GET(self):
        message = os.getenv("APP_MESSAGE", "My Unit 5 application")
        body = (message + "\n").encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)

port = int(os.getenv("PORT", "8080"))
print(f"Application listening on port {port}", flush=True)
HTTPServer(("0.0.0.0", port), App).serve_forever()
