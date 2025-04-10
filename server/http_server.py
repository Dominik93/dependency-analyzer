import http.server
import socketserver

DIRECTORY = "server"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)


def start_server(host, port):
    with socketserver.TCPServer((host, port), Handler) as httpd:
        print("Serving at " + host + ":" + str(port))
        httpd.serve_forever()
