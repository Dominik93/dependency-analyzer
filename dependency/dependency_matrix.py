from .module import Module
from .dependency import Dependency


class DependencyMatrix:
    modules: dict[str, Module] = {}

    dependencies: list[str] = []

    def __init__(self, modules: list[str], dependencies: list[str]):
        self.dependencies = dependencies
        self.modules = self.__init_dependencies_matrix(modules, dependencies)

    def __init_dependencies_matrix(self, modules: list[str], dependencies: list[str]) -> dict[str, Module]:
        matrix: dict[str, Module] = {}
        for module in modules:
            matrix[module] = Module(module)
            for dependency in dependencies:
                matrix[module].add_dependency(Dependency(dependency))
        return matrix

    def add_module(self, module: Module) -> None:
        self.modules[module.name] = module

    def get_module(self, module_name: str) -> Module:
        return self.modules[module_name]

    def get_dependency(self, module_name: str, dependency_name: str) -> Dependency:
        return self.get_module(module_name).get_dependency(dependency_name)

    def set_module_version(self, module_name: str, version: str) -> None:
        self.modules[module_name].set_version(version)

    def set_dependency_version_in_module(self, module_name: str, dependency_name: str, version: str) -> None:
        print('Set version in ' + module_name + ' of ' + dependency_name + ' to ' + version)
        self.modules[module_name].set_dependency_version(dependency_name, version)

    def get_all_modules(self):
        return self.modules.keys()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.modules)

    def __eq__(self, other):
        if not isinstance(other, DependencyMatrix):
            return NotImplemented

        return self.modules == other.modules and self.dependencies == other.dependencies
