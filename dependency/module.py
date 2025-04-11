from .dependency import Dependency


class Module:
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

    def _add_dependency(self, dependency: Dependency):
        self.dependencies[dependency.name] = dependency

    def _set_dependency_version(self, dependency_name, version):
        self._get_dependency(dependency_name)._set_version(version)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name + ':' + self.version + ' Dependencies: ' + str(self.dependencies)

    def __eq__(self, other):
        if not isinstance(other, Module):
            return NotImplemented

        return self.name == other.name and self.version == other.version and self.dependencies == other.dependencies
