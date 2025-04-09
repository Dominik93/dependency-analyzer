from .dependency_matrix import DependencyMatrix
from .maven import Maven


class DependenciesAnalyzer:
    modules = []
    dependencies = []
    maven = {}
    dependency_matrix: DependencyMatrix = {}

    def __init__(self, modules, dependencies):
        print('Modules: ' + str(modules))
        print('Dependencies: ' + str(dependencies))
        self.maven = Maven(dependencies)
        self.modules = modules
        self.dependency_matrix = DependencyMatrix(modules, dependencies)
        self.dependencies = dependencies

    def calculateDependencies(self):
        for module in self.modules:
            print('')
            print('Analize ' + module)
            dependency_tree = self.maven.dependency_tree(module)
            self.dependency_matrix.set_module_version(module, self.maven.find_module_version(module))
            for dependency in self.dependencies:
                if dependency in dependency_tree:
                    index_of_dependency = dependency_tree.find(dependency)
                    dependency_from_tree = dependency_tree[index_of_dependency: dependency_tree.find('\n', index_of_dependency)]
                    dependency_version = dependency_from_tree.split(':')[3]
                    self.dependency_matrix.set_dependency_version_in_module(module, dependency, dependency_version)
        return self.dependency_matrix
