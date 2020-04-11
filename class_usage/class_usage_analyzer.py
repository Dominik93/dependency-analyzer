import os
import re
import pickle

from class_usage.class_usage_matrix import ClassUsageMatrix

class ClassUsageAnalyzer:

    modules = []
    packages = []

    classRegexp  = ''

    matrix: ClassUsageMatrix = {}

    def __init__(self, modules, packages, classRegexp):
        self.matrix = ClassUsageMatrix(modules, packages)
        self.modules = modules
        self.packages = packages
        self.classRegexp = classRegexp

    def store(self):
        with open('store.class_usage_matrix', 'wb') as configFile:
            pickle.dump(self.matrix, configFile)

    def calcualteClassUsage(self):
        for module in self.modules.get():
            projectPath = os.getcwd() + '/temp/' + module.name
            print('Analize ' + module.name)
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
                                        self.matrix.addDependencyClassInModule(module.name, package, classWithPackage)
        return self.matrix

    def __stripImport(self, string):
        return string.replace('import ', '').replace('\n', '').replace(';', '')
