from class_usage.class_usage_dependency import ClassUsageDependency

class ClassUsageModule:

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

    def _addDependency(self, dependency: ClassUsageDependency):
        self.dependencies[dependency.name] = dependency

    def _addDependencyClass(self, dependencyName, aClass):
        self._getDependency(dependencyName)._addClass(aClass)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.name) + ':' + str(self.version) + ' Class usages: ' + str(self.dependencies)
