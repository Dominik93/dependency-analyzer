from list_util import maxLength
from .dependency_matrix import DependencyMatrix


class DependencyPriter:

    SEPARATOR = '  |  '
    dependencyMatrix = {}

    moduleWidth = 0
    dependencyWidth = 0

    def __init__(self, dependencyMatrix: DependencyMatrix):
        self.dependencyMatrix = dependencyMatrix
        modulesWithVersion = self.__addVersion(self.dependencyMatrix.getAllModules())
        self.moduleWidth = maxLength(modulesWithVersion)
        self.dependencyWidth = maxLength(map(self.__retriveDependency, self.dependencyMatrix.dependencies)) 

    def printDependencyMatrix(self):
        print('Dependency matrix:')
        self.__printHeaders()
        self.__printRowSeparator()
        self.__printContent()
        self.__printRowSeparator()

    def __retriveDependency(self,string): 
        return string.split(':')[1]

    def __printRowSeparator(self):
        rowSeparator = ''.ljust(self.moduleWidth, '-') + '-----'
        for dependency in self.dependencyMatrix.dependencies:
            rowSeparator += ''.ljust(self.dependencyWidth, '-') + '-----'
        print(rowSeparator)

    def __printHeaders(self):
        dependenciesHeaders = ''.ljust(self.moduleWidth, ' ') + self.SEPARATOR
        for dependency in self.dependencyMatrix.dependencies:
            dependenciesHeaders += self.__retriveDependency(dependency).ljust(self.dependencyWidth, ' ') + self.SEPARATOR
        print(dependenciesHeaders)
          
    def __printContent(self):
        for module in self.dependencyMatrix.getAllModules():
            self.__printRow(module)

    def __printRow(self, module):
        moduleRow = (module + ' ' + self.dependencyMatrix.getModule(module).version).ljust(self.moduleWidth, '.') + self.SEPARATOR
        for dependency in self.dependencyMatrix.dependencies:
            moduleRow += self.dependencyMatrix.getDependency(module, dependency).version.ljust(self.dependencyWidth, ' ') + self.SEPARATOR
        print(moduleRow)

    def __addVersion(self, modules):
        modulesWithVersion = []
        for module in modules:
            modulesWithVersion.append(module + ' ' + self.dependencyMatrix.getModule(module).version)
        return modulesWithVersion