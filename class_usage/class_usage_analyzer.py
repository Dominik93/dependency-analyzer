import os
import re
from .class_usage_matrix import ClassUsageMatrix

class ClassUsageAnalyzer:

    modules = []
    packages = []

    classRegexp  = ''

    matix: ClassUsageMatrix = {}

    def __init__(self, modules, packages, classRegexp):
        self.matrix = ClassUsageMatrix(modules, packages)
        self.modules = modules
        self.packages = packages
        self.classRegexp = classRegexp

    def calcualteClassUsage(self):
        for module in self.modules:
            projectPath = os.getcwd() + '/temp/' + module
            print('Analize ' + module)
            for (dirpath, dirnames, filenames) in os.walk(projectPath):
                for file in filenames:
                    if '.java' in file:
                        path = dirpath + '\\' + file
                        f = open(path, "r", encoding = "utf8")
                        lines = f.readlines()
                        f.close()
                        for line in lines:
                            for package in self.packages:
                                if package in line and 'import' in line: 
                                    classWithPackage = self.__stripImport(line)
                                    if re.search(self.classRegexp, classWithPackage):
                                        self.matrix.addDependencyClassInModule(module, package, classWithPackage)
        return self.matrix

    def __stripImport(self, string):
        return string.replace('import ', '').replace('\n', '').replace(';', '')
