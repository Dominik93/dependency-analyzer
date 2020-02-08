import os
import schedule
import threading
import configparser
import argparse
import time
from list_util import stripArray
from init_live import modules, packages, dependencies, gitUrl, branch,intervalInMunites, classRegexp, printStrategy, host, port
from server.http_server import startServer
from analyze import analyzeClassUsage, analyzeDependencies, cloneAllProjects

cloneAllProjects(gitUrl, branch, modules)
serverThread = threading.Thread(target=startServer, args=(host, port,))
serverThread.daemon = True
serverThread.start()

schedule.every(intervalInMunites).minutes.do(lambda : analyzeDependencies(modules, dependencies, printStrategy))
schedule.every(intervalInMunites).minutes.do(lambda : analyzeClassUsage(modules, packages, classRegexp, printStrategy))
while True:
    schedule.run_pending()
    time.sleep(1)
schedule.clear()    