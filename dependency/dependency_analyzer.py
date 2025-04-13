from maven.pom_loader import find_module_version
from .dependency_matrix import DependencyMatrix
from maven.maven import Maven


class DependenciesAnalyzer:
    modules: list[str] = []
    dependencies: list[str] = []
    maven: Maven = {}
    dependency_matrix: DependencyMatrix = {}

    def __init__(self, maven: Maven, modules: list[str], dependencies: list[str]):
        print('Modules: ' + str(modules))
        print('Dependencies: ' + str(dependencies))
        self.maven = maven
        self.modules = modules
        self.dependency_matrix = DependencyMatrix(modules, dependencies)
        self.dependencies = dependencies

    def calculate_dependencies(self) -> DependencyMatrix:
        for module in self.modules:
            print('\nAnalyze ' + module)
            dependency_tree = self.maven.dependency_tree(module)
            sanitized_dependency_tree = "\n".join(filter(lambda x: "[INFO]" in x, dependency_tree.splitlines()))
            self.dependency_matrix.set_module_version(module, find_module_version(module))
            for dependency in self.dependencies:
                if dependency in sanitized_dependency_tree:
                    index_of_dependency_start = sanitized_dependency_tree.find(dependency)
                    index_of_dependency_end = sanitized_dependency_tree.find('\n', index_of_dependency_start)
                    dependency_from_tree = sanitized_dependency_tree[index_of_dependency_start: index_of_dependency_end]
                    dependency_version = dependency_from_tree.split(':')[3]
                    self.dependency_matrix.set_dependency_version_in_module(module, dependency, dependency_version)
        return self.dependency_matrix
