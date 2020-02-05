import os
from list_util import maxLength

class UsageAnalyzer:

    modules = []
    packages = []

    usageMatrix = {}

    def __init__(self, modules, packages):
        self.modules = modules
        self.packages = packages

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
                        f = open(path, "r", encoding="utf8")
                        lines = f.readlines()
                        f.close()
                        for line in lines:
                            for package in self.packages:
                                if package in line and 'import' in line: 
                                    self.usageMatrix[module][package].add(self.stripImport(line))
        return self.usageMatrix

    def stripImport(self, string):
        return string.replace('import ', '').replace('\n', '').replace(';', '')
