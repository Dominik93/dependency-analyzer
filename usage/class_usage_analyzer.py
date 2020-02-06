import os
import re
from list_util import maxLength

class ClassUsageAnalyzer:

    modules = []
    packages = []

    classRegexp  = ''

    usageMatrix = {}

    def __init__(self, modules, packages, classRegexp):
        self.modules = modules
        self.packages = packages
        self.classRegexp = classRegexp

        self.usageMatrix = self.initUsageMatrix()

    def retrivePackage(self, string): 
        return string.split(':')[0]

    def initUsageMatrix(self):
        matrix = {}        
        for module in self.modules:
            matrix[module] = {}
            for package in self.packages:
                matrix[module][package] = set([])
        return matrix

    def calcualteUsage(self):
        for module in self.modules:
            projectPath = os.getcwd() + '/' + module
            print('Analize ' + module)
            for (dirpath, dirnames, filenames) in os.walk(projectPath):
                for file in filenames:
                    if '.java' in file:
                        path = dirpath + '\\' + file
                        f = open(path, "r")
                        #f = open(path, "r", encoding = "utf8")
                        lines = f.readlines()
                        f.close()
                        for line in lines:
                            for package in self.packages:
                                if package in line and 'import' in line: 
                                    classWithPackage = self.stripImport(line)
                                    if re.search(self.classRegexp, classWithPackage):
                                        self.usageMatrix[module][package].add(classWithPackage)
        return self.usageMatrix

    def stripImport(self, string):
        return string.replace('import ', '').replace('\n', '').replace(';', '')
