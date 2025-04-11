import http

import schedule
import threading
import time
from init.init_live import modules, packages, dependencies, git_url, branch, interval_in_munites, class_regexp, \
    print_strategy, host, port
from server.http_server import start_server
from analyze import analyze_class_usage, analyze_dependencies, clone_all_projects
import http.server


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='server', **kwargs)


if __name__ == '__main__':
    clone_all_projects(git_url, branch, modules)
    server_thread = threading.Thread(target=start_server, args=(host, port, Handler))
    server_thread.daemon = True
    server_thread.start()

    schedule.every(interval_in_munites).minutes.do(
        lambda: analyze_dependencies('server/', modules, dependencies, print_strategy))
    schedule.every(interval_in_munites).minutes.do(
        lambda: analyze_class_usage(modules, packages, class_regexp, print_strategy))
    while True:
        schedule.run_pending()
        time.sleep(1)
