import schedule
import threading
import time
from init.init_live import modules, packages, dependencies, git_url, branch, interval_in_minutes, class_regexp, \
    print_strategy, host, port, directory
from server.http_server import start_server
from analyze import analyze_class_usage, analyze_dependencies, clone_all_projects
import http.server

server_path = "server"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=server_path, **kwargs)


if __name__ == '__main__':
    clone_all_projects(directory, git_url, branch, modules)
    server_thread = threading.Thread(target=start_server, args=(host, port, Handler))
    server_thread.daemon = True
    server_thread.start()
    analyze_dependencies(directory, server_path, modules, dependencies, print_strategy)
    analyze_class_usage(directory, server_path, modules, packages, class_regexp, print_strategy)

    schedule.every(interval_in_minutes).minutes.do(
        lambda: analyze_dependencies(directory, server_path, modules, dependencies, print_strategy))
    schedule.every(interval_in_minutes).minutes.do(
        lambda: analyze_class_usage(directory, server_path, modules, packages, class_regexp, print_strategy))
    while True:
        schedule.run_pending()
        time.sleep(1)
