import http.server
import threading
import time
import schedule
from analyze import analyze_class_usage, analyze_dependencies, clone_all_projects
from init.init_live import init
from printer_manager import PrinterManager
from server.http_server import start_server

server_path = "server"


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=server_path, **kwargs)


def _analyze(directory: str, server_path: str, modules: list[str], dependencies: list[str],
             packages: list[str], class_regexp: str, prints_strategy: str):
    manager = PrinterManager(prints_strategy, server_path)

    dependency_matrix = analyze_dependencies(directory, modules, dependencies)
    class_usage_matrix = analyze_class_usage(directory, modules, packages, class_regexp)

    manager.set_dependency_matrix(dependency_matrix)
    manager.set_class_usage_matrix(class_usage_matrix)
    manager.set_modules(modules, dependency_matrix, class_usage_matrix)

    manager.get_dependency_printer().print()
    manager.get_class_usage_printer().print()
    manager.get_modules_printer().print()


if __name__ == '__main__':
    configuration = init()
    server_configuration = configuration.server_configuration
    git_configuration = configuration.git_configuration
    project_configuration = configuration.project_configuration
    analyze_configuration = configuration.analyze_configuration

    clone_all_projects(project_configuration.directory, git_configuration.git_url, git_configuration.branch,
                       analyze_configuration.modules)
    server_thread = threading.Thread(target=start_server,
                                     args=(server_configuration.host, server_configuration.port, Handler))
    server_thread.daemon = True
    server_thread.start()

    _analyze(project_configuration.directory, server_path, analyze_configuration.modules,
             analyze_configuration.dependencies, analyze_configuration.packages, analyze_configuration.class_regexp,
             configuration.print_strategy)

    if configuration.interval_in_minutes is not None:
        schedule.every(configuration.interval_in_minutes).minutes.do(
            lambda: _analyze(project_configuration.directory, server_path, analyze_configuration.modules,
                             analyze_configuration.dependencies, analyze_configuration.packages,
                             analyze_configuration.class_regexp, analyze_configuration.print_strategy))

    while True:
        schedule.run_pending()
        time.sleep(1)
