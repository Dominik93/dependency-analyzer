from .class_usage_dependency import ClassUsageDependency


class ClassUsageModule:
    name: str = ''

    version: str = 'unknown'

    dependencies: dict[str, ClassUsageDependency] = {}

    def __init__(self, name: str):
        self.name = name
        self.version = 'unknown'
        self.dependencies = {}

    def set_version(self, version: str) -> None:
        self.version = version

    def get_dependency(self, dependency_name: str) -> ClassUsageDependency:
        return self.dependencies[dependency_name]

    def add_dependency(self, dependency: ClassUsageDependency) -> None:
        self.dependencies[dependency.name] = dependency

    def add_dependency_class(self, dependency_name: str, a_class: str) -> None:
        self.get_dependency(dependency_name).add_class(a_class)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name + ':' + self.version + ' Class usages: ' + str(self.dependencies)

    def __eq__(self, other):
        if not isinstance(other, ClassUsageModule):
            return NotImplemented

        return self.name == other.name and self.version == other.version and self.dependencies == other.dependencies
