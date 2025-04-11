from ..dependency_matrix import DependencyMatrix


class ConsoleDependencyPrinter:

    def __init__(self, content):
        self.content = content

    def print(self):
        print(self.content)
