import os

from maven.executor import Executor


class OsExecutor(Executor):

    def getcwd(self) -> str:
        return os.getcwd()

    def execute(self, command) -> str:
        print('execute: ' + command)
        return os.popen(command).read()
