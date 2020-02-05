from .dependency import Dependency


class Module:

    name = ''

    version = ''

    dependencies = {}

    def __init__(self, name):
        self.name = name

    def _setVersion(self, version):
        self.version = version

    def _getDependency(self, dependencyName):
        return self.dependencies[dependencyName]

    def _addDependency(self, dependency: Dependency):
        self.dependencies[dependency.name] = dependency

    def _setDependencyVersion(self, dependencyName, version):
        self.dependencies[dependencyName]._setVersion(version)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name + ':' + self.version + ' Dependencies ' + str(self.dependencies)
