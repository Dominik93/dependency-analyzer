from .module import Module
from .dependency import Dependency


class DependencyMatrix:
    modules = {}

    dependencies = []

    def __init__(self, modules, dependencies):
        self.dependencies = dependencies
        self.modules = self.__init_dependencies_matrix(modules, dependencies)

    def __init_dependencies_matrix(self, modules, dependencies):
        matrix = {}
        for module in modules:
            matrix[module] = Module(module)
            for dependency in dependencies:
                matrix[module]._add_dependency(Dependency(dependency))
        return matrix

    def add_module(self, module: Module):
        self.modules[module.name] = module

    def get_module(self, module_name):
        return self.modules[module_name]

    def get_dependency(self, module_name, dependency_name):
        return self.get_module(module_name)._get_dependency(dependency_name)

    def set_module_version(self, module_name, version):
        self.modules[module_name]._set_version(version)

    def set_dependency_version_in_module(self, module_name, dependency_name, version):
        print('Set version in ' + module_name + ' of ' + dependency_name + ' to ' + version)
        self.modules[module_name]._set_dependency_version(dependency_name, version)

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
