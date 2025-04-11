from ..dependency_matrix import DependencyMatrix


class FileDependencyPrinter:

    def __init__(self, content, dir_path):
        self.content = content
        self.dir_path = dir_path

    def print(self):
        f = open(self.dir_path + "/dependencies.html", 'w')
        f.write(self.content)
        f.close()
