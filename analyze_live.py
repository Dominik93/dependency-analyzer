import schedule
import threading
import time
from init.init_live import modules, packages, dependencies, gitUrl, branch, intervalInMunites, class_regexp, \
    print_strategy, host, port
from server.http_server import startServer
from analyze import analyze_class_usage, analyze_dependencies, clone_all_projects

clone_all_projects(gitUrl, branch, modules)
serverThread = threading.Thread(target=startServer, args=(host, port,))
serverThread.daemon = True
serverThread.start()

schedule.every(intervalInMunites).minutes.do(lambda: analyze_dependencies(modules, dependencies, print_strategy))
schedule.every(intervalInMunites).minutes.do(lambda: analyze_class_usage(modules, packages, class_regexp, print_strategy))
while True:
    schedule.run_pending()
    time.sleep(1)
