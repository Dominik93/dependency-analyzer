from .class_usage_module import ClassUsageModule
from .class_usage_dependency import ClassUsageDependency


class ClassUsageMatrix:
    modules = {}

    dependencies = []

    def __init__(self, modules, dependencies):
        self.dependencies = dependencies
        self.modules = self.__init_dependencies_matrix(modules, dependencies)

    def __init_dependencies_matrix(self, modules, dependencies):
        matrix = {}
        for module in modules:
            matrix[module] = ClassUsageModule(module)
            for dependency in dependencies:
                matrix[module]._add_dependency(ClassUsageDependency(dependency))
        return matrix

    def add_module(self, module: ClassUsageModule):
        self.modules[module.name] = module

    def get_module(self, module_name):
        return self.modules[module_name]

    def get_dependency(self, module_name, dependency_name):
        return self.get_module(module_name)._get_dependency(dependency_name)

    def set_module_version(self, module_name, version):
        self.modules[module_name]._set_version(version)

    def add_dependency_class_in_module(self, module_name, dependency_name, a_class):
        self.modules[module_name]._add_dependency_class(dependency_name, a_class)

    def get_all_modules(self):
        return self.modules.keys()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.modules)
