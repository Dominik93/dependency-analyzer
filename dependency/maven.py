import os


class Maven:

    def __init__(self, dependencies):
        self.includesOption = self.__dependencies_to_includes_option(dependencies)

    def dependencyTree(self, module):
        project_path = os.getcwd() + '/temp/' + module
        return os.popen('mvn -f ' + project_path + ' dependency:tree ' + self.includesOption).read()

    def find_module_version(self, module):
        project_path = os.getcwd() + '/temp/' + module
        return os.popen(
            'mvn -f ' + project_path + ' org.apache.maven.plugins:maven-help-plugin:evaluate -Dexpression=project.version | findstr /v /R /C:"^\[INFO\].*" | findstr /v /R /C:"^Down.*"').read().replace(
            '\n', '')

    def __dependencies_to_includes_option(self, dependencies):
        str = ''
        for dependency in dependencies:
            str = str + dependency + ' '
        return '-Dincludes=' + str.strip().replace(' ', ',')
