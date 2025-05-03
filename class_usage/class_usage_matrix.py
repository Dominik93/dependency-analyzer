from typing import Callable

from .class_usage_dependency import ClassUsageDependency
from .class_usage_module import ClassUsageModule


class ClassUsageMatrix:
    modules = {}

    dependencies: list[str] = []

    def __init__(self, modules: list[str], dependencies: list[str]):
        self.dependencies = dependencies
        self.modules = self.__init_dependencies_matrix(modules, dependencies)

    def __init_dependencies_matrix(self, modules: list[str], dependencies: list[str]):
        matrix = {}
        for module in modules:
            matrix[module] = ClassUsageModule(module)
            for dependency in dependencies:
                matrix[module].add_dependency(ClassUsageDependency(dependency))
        return matrix

    def get_module(self, module_name):
        return self.modules[module_name]

    def get_dependency(self, module_name, dependency_name):
        return self.get_module(module_name).get_dependency(dependency_name)

    def set_module_version(self, module_name, version):
        print(f'Set version of {module_name} to {version}')
        self.modules[module_name].set_version(version)

    def add_dependency_class_in_module(self, module_name: str, dependency_name: str, a_class: str):
        print(f'To {module_name} add {dependency_name} with class {a_class}')
        self.modules[module_name].add_dependency_class(dependency_name, a_class)

    def get_all_modules(self):
        return self.modules.keys()

    def get_modules(self, filter_fn: Callable):
        return list(filter(filter_fn, self.get_all_modules()))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.modules)

    def __eq__(self, other):
        if not isinstance(other, ClassUsageMatrix):
            return NotImplemented

        return self.modules == other.modules and self.dependencies == other.dependencies
