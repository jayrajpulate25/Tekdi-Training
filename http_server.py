# HTTP Practice
# Baseline Course

from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Handle GET request
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>GET Request Received</h1></body></html>")

    def do_POST(self):
        # Handle POST request
        content_length = int(self.headers['Content-Length'])  # Get the size of the data
        post_data = self.rfile.read(content_length)  # Read the POST data

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        response = f'{{"message": "POST received", "data": "{post_data.decode()}"}}'
        self.wfile.write(response.encode())

    def do_PUT(self):
        # Handle PUT request
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"PUT Request Received")

    def do_DELETE(self):
        # Handle DELETE request
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"DELETE Request Received")

if __name__ == "__main__":
    # Define server address and port
    server_address = ('', 8000)  # '' makes the server accessible from any network interface
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()
