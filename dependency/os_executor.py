import os

from maven.executor import Executor


class OsExecutor(Executor):

    def execute(self, command) -> str:
        print(f'execute: {command}')
        return os.popen(command).read()
