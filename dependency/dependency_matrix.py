from .module import Module
from .dependency import Dependency

class DependencyMatrix:

    modules = {}

    dependencies = []

    def __init__(self, modules, dependencies):
        self.dependencies = dependencies
        self.modules = self.__initDependenciesMatrix(modules, dependencies)

    def __initDependenciesMatrix(self, modules, dependencies):
        matrix = {}        
        for module in modules:
            matrix[module] = Module(module)
            for dependency in dependencies:
                matrix[module]._addDependency(Dependency(dependency))
        return matrix

    def addModule(self, module: Module):
        self.modules[module.name] = module

    def getModule(self, moduleName):
        return self.modules[moduleName]  

    def getDependency(self, moduleName, dependencyName):
        return self.getModule(moduleName)._getDependency(dependencyName)

    def setModuleVersion(self, moduleName, version):
        self.modules[moduleName]._setVersion(version)    

    def setDependencyVersionInModule(self, moduleName, dependencyName, version):
        print('Set version in ' + moduleName + ' of ' + dependencyName + ' to ' + version)
        self.modules[moduleName]._setDependencyVersion(dependencyName, version)

    def getAllModules(self):
        return self.modules.keys()  
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.modules)
    