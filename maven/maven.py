import os
import xmltodict

from maven.executor import Executor


class Maven:

    def __init__(self, executor: Executor, dependencies):
        self.executor = executor
        self.includes_option = self.__dependencies_to_includes_option(dependencies)

    def dependency_tree(self, module):
        project_path = self.executor.getcwd() + '/temp/' + module
        command = 'mvn -f ' + project_path + ' dependency:tree ' + self.includes_option
        return self.executor.execute(command)

    def find_module_version(self, module):
        project_path = os.getcwd() + '/temp/' + module + "/pom.xml"
        with open(project_path, "rb") as file:
            pom = xmltodict.parse(file)
            return pom['project']['version']

    def __dependencies_to_includes_option(self, dependencies):
        str = ''
        for dependency in dependencies:
            str = str + dependency + ' '
        return '-Dincludes=' + str.strip().replace(' ', ',')


