import os


class Maven:

    def __init__(self):
        pass

    def dependencyTree(self, module, dependencies):
        projectPath = os.getcwd() + '/temp/' + module.name
        includesOption = self.__dependenciesToIncludesOption(dependencies)
        return os.popen('mvn -f ' + projectPath + ' dependency:tree ' + includesOption).read()

    def findModuleVersion(self, module):
        print('Find version of ' + module)
        projectPath = os.getcwd() + '/temp/' + module
        return os.popen('mvn -f ' + projectPath + ' org.apache.maven.plugins:maven-help-plugin:evaluate -Dexpression=project.version | findstr /v /R /C:"^\[INFO\].*" | findstr /v /R /C:"^Down.*"').read().replace('\n', '')

    def __dependenciesToIncludesOption(self, dependencies):
        str = ''
        for dependency in dependencies.get():
            str = str + dependency.getName() + ' '
        return '-Dincludes=' + str.strip().replace(' ', ',')
