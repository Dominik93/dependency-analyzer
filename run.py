
import os
import time
import schedule
import threading

from server.http_server import startServer
from init.init_live import rawModules, rawPackages, rawDependencies, gitUrl, branch, intervalInMunites, classRegexp, host, port
from maven.maven import Maven
from dependency.dependency_factory import DependencyFactory
from dependency.dependency_analyzer import DependenciesAnalyzer
from dependency.dependencies_scheduler import DependenciesScheduler
from dependency.dependency_scheduler import DependencyScheduler
from dependency.dependencies import Dependencies
from class_usage.class_usage_scheduler import ClassUsageScheduler
from subscription.subscription_scheduler import SubscriptionScheduler
from module.module_factory import ModuleFactory
from module.modules_scheduler import ModulesScheduler
from module.modules import Modules
from printer.printer_scheduler import PrinterScheduler
from git.git import Git


path = os.getcwd() + '/temp/'
git = Git(gitUrl, branch, path)
maven = Maven()

serverThread = threading.Thread(target=startServer, args=(host, port,))
serverThread.daemon = True
serverThread.start()


depScheduler = DependenciesScheduler(git, maven, intervalInMunites)
#depScheduler.add(schedule, rawDependencies)

modScheduler = ModulesScheduler(git, maven, intervalInMunites)
#modScheduler.add(schedule, rawModules)

depMatrix = DependencyScheduler(maven, intervalInMunites, DependencyFactory(git, maven), ModuleFactory(git, maven))
#depMatrix.add(schedule, rawModules, rawDependencies)


classUsageScheduler = ClassUsageScheduler(intervalInMunites, Modules(), rawPackages, classRegexp)
#classUsageScheduler.run()

printerScheduler = PrinterScheduler(intervalInMunites, Modules(), Dependencies())
printerScheduler.run()

subscriptionScheduler = SubscriptionScheduler(intervalInMunites, Dependencies())
subscriptionScheduler.run()

while True:
    schedule.run_pending()
    time.sleep(1)
schedule.clear()   


# run dependency scheduler
    # load from config
    # calcualte depenendcies
    # store dependencies
# run class usage scheduler
    # load from config
    # calcualte class usage
    # store class usage
# run subscription scheduler
    # load from config 
    # run dependency
    # if stored dependencies exist calculate difference
    # send notifications
    # store depenecies
# run server for visualization dependencies and class usage