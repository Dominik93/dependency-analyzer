import os
from list_util import maxLength
from .dependency_matrix import DependencyMatrix
from .maven import Maven

class DependenciesAnalyzer:

    modules = []
    dependencies = []
    maven = {}
    dependencyMatrix : DependencyMatrix = {}

    def __init__(self, modules, dependencies):
        print('Modules: ' + str(modules))
        print('Dependencies: ' + str(dependencies))
        self.maven = Maven(dependencies)
        self.modules = modules
        self.dependencyMatrix = DependencyMatrix(modules, dependencies)
        self.dependencies = dependencies

    def calculateDependencies(self):
        for module in self.modules:
            print('')
            print('Analize ' + module)
            dependencyTree = self.maven.dependencyTree(module)
            self.dependencyMatrix.setModuleVersion(module, self.maven.findModuleVersion(module))
            for dependency in self.dependencies:
                if dependency in dependencyTree:
                    indexOfDependency = dependencyTree.find(dependency)
                    dependencyFromTree = dependencyTree[indexOfDependency: dependencyTree.find('\n', indexOfDependency)]
                    dependencyVersion = dependencyFromTree.split(':')[3] 
                    self.dependencyMatrix.setDependencyVersionInModule(module, dependency, dependencyVersion)
        return self.dependencyMatrix