import os
from list_util import maxLength

class DependenciesAnalyzer:

    modules = []
    dependencies = []

    dependencyMatrix = {}

    def __init__(self, modules, dependencies):
        self.modules = modules
        self.dependencies = dependencies
        self.dependencyMatrix = self.initDependenciesMatrix()

    def initDependenciesMatrix(self):
        matrix = {}        
        for module in self.modules:
            matrix[module] = {}
            for dependency in self. dependencies:
                matrix[module]['_version'] = 'unknown'
                matrix[module][dependency] = ''
        return matrix

    def calculateDependencies(self):
        print('Dependencies: ' + str(self.dependencies))
        includesOption = self.dependenciesToIncludesOption()
        for module in self.modules:
            projectPath = os.getcwd() + '/' + module
            print('Analize ' + module)
            dependencyTree = os.popen('mvn -f ' + projectPath + ' dependency:tree ' + includesOption).read()
            self.dependencyMatrix[module]['_version'] = self.findModuleVersion(projectPath)
            for dependency in self.dependencies:
                if dependency in dependencyTree:
                    indexOfDependency = dependencyTree.find(dependency)
                    dependencyFromTree = dependencyTree[indexOfDependency: dependencyTree.find('\n', indexOfDependency)]
                    dependencyVersion = dependencyFromTree.split(':')[3] 
                    self.dependencyMatrix[module][dependency] = dependencyVersion
                    print('Found ' + dependency +'\tversion: ' + dependencyVersion)
                else:
                    self.dependencyMatrix[module][dependency] = ''  
        return self.dependencyMatrix

    def dependenciesToIncludesOption(self):
        str = ''
        for dependency in self.dependencies:
            str = str + dependency+ ' '
        return '-Dincludes=' + str.strip().replace(' ', ',')

    def findModuleVersion(self, projectPath):
        return os.popen('mvn -f ' + projectPath + ' org.apache.maven.plugins:maven-help-plugin:evaluate -Dexpression=project.version | findstr /v /R /C:"^\[INFO\].*"').read().replace('\n', '')
