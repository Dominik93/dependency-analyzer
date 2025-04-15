from .dependency import Dependency


class Module:
    name: str = ''

    version: str = 'unknown'

    dependencies: dict[str, Dependency] = {}

    def __init__(self, name):
        self.name = name
        self.version = 'unknown'
        self.dependencies = {}

    def set_version(self, version: str) -> None:
        print(f'Set {self.name} to {version}')
        self.version = version

    def get_dependency(self, dependency_name: str) -> Dependency:
        return self.dependencies[dependency_name]

    def add_dependency(self, dependency: Dependency) -> None:
        self.dependencies[dependency.name] = dependency

    def set_dependency_version(self, dependency_name: str, version: str) -> None:
        print(f'Set {dependency_name} to {version}')
        self.get_dependency(dependency_name).set_version(version)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name + ':' + self.version + ' Dependencies: ' + str(self.dependencies)

    def __eq__(self, other):
        if not isinstance(other, Module):
            return NotImplemented

        return self.name == other.name and self.version == other.version and self.dependencies == other.dependencies
