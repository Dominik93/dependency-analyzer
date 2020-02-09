from ..dependency_matrix import DependencyMatrix

class ConsoleDependencyPrinter:

    SEPARATOR = '  |  '
    ROW_SEPARATOR = '-----'
    dependencyMatrix = {}

    moduleWidth = 0
    dependencyWidth = 0

    def __init__(self, dependencyMatrix: DependencyMatrix):
        self.dependencyMatrix = dependencyMatrix
        modulesWithVersion = self.__addVersion(self.dependencyMatrix.getAllModules())
        self.moduleWidth = len(max(modulesWithVersion, key=len))
        self.dependencyWidth = len(max(map(self.__retriveDependency, self.dependencyMatrix.dependencies), key=len))

    def printDependencyMatrix(self):
        print('Dependency matrix:')
        self.__printHeaders()
        self.__printRowSeparator()
        self.__printContent()
        self.__printRowSeparator()

    def __retriveDependency(self,string): 
        return string.split(':')[1]

    def __printRowSeparator(self):
        rowSeparator = ''.ljust(self.moduleWidth, '-') + self.ROW_SEPARATOR
        size = len(self.dependencyMatrix.dependencies)
        i = 0 
        while i < size:
            rowSeparator += ''.ljust(self.dependencyWidth, '-') + self.ROW_SEPARATOR
            i += 1
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
        
    def __maxLength(self, array):
        length = 0
        for item in array:
            if len(item) > length:
                length = len(item)
        return length        

    def __addVersion(self, modules):
        modulesWithVersion = []
        for module in modules:
            modulesWithVersion.append(module + ' ' + self.dependencyMatrix.getModule(module).version)
        return modulesWithVersion