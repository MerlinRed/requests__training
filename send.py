import time
import requests
from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ('', 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

with requests.Session() as session:
    while True:
        time.sleep(1)
        send = session.get('http://localhost:9000')
        print(f'Я отправил GET запрос на {send.request.url}')

httpd.serve_forever()
