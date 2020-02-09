import os

class Maven:

    def __init__(self, dependencies):
        self.includesOption = self.__dependenciesToIncludesOption(dependencies)

    def dependencyTree(self, module):
        projectPath = os.getcwd() + '/temp/' + module
        return  os.popen('mvn -f ' + projectPath + ' dependency:tree ' + self.includesOption).read()
    
    def findModuleVersion(self, module):
        projectPath = os.getcwd() + '/temp/' + module
        return os.popen('mvn -f ' + projectPath + ' org.apache.maven.plugins:maven-help-plugin:evaluate -Dexpression=project.version | findstr /v /R /C:"^\[INFO\].*" | findstr /v /R /C:"^Down.*"').read().replace('\n', '')

    def __dependenciesToIncludesOption(self, dependencies):
        str = ''
        for dependency in dependencies:
            str = str + dependency + ' '
        return '-Dincludes=' + str.strip().replace(' ', ',')
