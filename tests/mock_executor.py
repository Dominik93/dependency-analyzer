from maven.executor import Executor


class MockExecutor(Executor):

    def __init__(self, mocks):
        self.mocks = mocks

    def execute(self, command):
        return self.mocks[command]
