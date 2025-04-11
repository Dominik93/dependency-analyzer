from dependency.executor import Executor


class MockExecutor(Executor):

    def __init__(self, cwd, mocks):
        self.mocks = mocks
        self.cwd = cwd

    def getcwd(self):
        return self.cwd

    def execute(self, command):
        return self.mocks[command]
