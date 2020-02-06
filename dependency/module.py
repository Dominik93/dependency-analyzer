from .dependency import Dependency


class Module:

    name = ''

    version = 'unknown'

    dependencies = {}

    def __init__(self, name):
        self.name = name
        self.version = 'unknown'
        self.dependencies = {}

    def _setVersion(self, version):
        self.version = version

    def _getDependency(self, dependencyName):
        return self.dependencies[dependencyName]

    def _addDependency(self, dependency: Dependency):
        self.dependencies[dependency.name] = dependency

    def _setDependencyVersion(self, dependencyName, version):
        self._getDependency(dependencyName)._setVersion(version)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name + ':' + self.version + ' Dependencies: ' + str(self.dependencies)
