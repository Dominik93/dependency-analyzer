import socketserver


def start_server(host, port, handler_class):
    with socketserver.TCPServer((host, port), handler_class) as httpd:
        print("Serving at " + host + ":" + str(port))
        httpd.serve_forever()
