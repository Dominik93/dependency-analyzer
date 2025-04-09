from .class_usage_dependency import ClassUsageDependency


class ClassUsageModule:
    name = ''

    version = 'unknown'

    dependencies = {}

    def __init__(self, name):
        self.name = name
        self.version = 'unknown'
        self.dependencies = {}

    def _set_version(self, version):
        self.version = version

    def _get_dependency(self, dependency_name):
        return self.dependencies[dependency_name]

    def _add_dependency(self, dependency: ClassUsageDependency):
        self.dependencies[dependency.name] = dependency

    def _add_dependency_class(self, dependency_name, a_class):
        self._get_dependency(dependency_name)._add_class(a_class)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name + ':' + self.version + ' Class usages: ' + str(self.dependencies)
