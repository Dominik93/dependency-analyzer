import os

from maven.executor import Executor


class OsExecutor(Executor):

    def execute(self, command) -> str:
        print(f'{os.getpid()}: execute: {command[:180]}')
        return os.popen(command).read()
