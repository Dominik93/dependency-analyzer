
from class_usage.class_usage_module import ClassUsageModule
from class_usage.class_usage_dependency import ClassUsageDependency

class ClassUsageMatrix:

    modules = {}

    dependencies = []

    def __init__(self, modules, dependencies):
        self.dependencies = dependencies
        self.modules = self.__initDependenciesMatrix(modules, dependencies)

    def __initDependenciesMatrix(self, modules, dependencies):
        matrix = {}        
        for module in modules.get():
            matrix[module.name] = ClassUsageModule(module.name)
            for dependency in dependencies:
                matrix[module.name]._addDependency(ClassUsageDependency(dependency))
        return matrix

    def addModule(self, module: ClassUsageModule):
        self.modules[module.name] = module

    def getModule(self, moduleName):
        return self.modules[moduleName]  

    def getDependency(self, moduleName, dependencyName):
        return self.getModule(moduleName)._getDependency(dependencyName)

    def setModuleVersion(self, moduleName, version):
        self.modules[moduleName]._setVersion(version)    

    def addDependencyClassInModule(self, moduleName, dependencyName, aClass):
        self.modules[moduleName]._addDependencyClass(dependencyName, aClass)

    def getAllModules(self):
        return self.modules.keys()  
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.modules)
    