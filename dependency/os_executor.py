import os

from dependency.executor import Executor


class OsExecutor(Executor):

    def getcwd(self):
        return os.getcwd()
    def execute(self, command):
        print('execute: ' + command)
        return os.popen(command).read()
