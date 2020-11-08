from http.server import HTTPServer, BaseHTTPRequestHandler


class HandlerRequests(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.address_string()

    def do_GET(self):
        self._set_headers()
        print(f'Я получил GET запрос от {self.address_string()}')


server_address = ('', 9000)
httpd = HTTPServer(server_address, HandlerRequests)
httpd.serve_forever()
