from maven.executor import Executor


class Maven:

    def __init__(self, directory: str, executor: Executor, dependencies: list[str]):
        self.executor = executor
        self.directory = directory
        self.includes_option = self.__dependencies_to_includes_option(dependencies)

    def dependency_tree(self, module: str) -> str:
        project_path = self.directory + "/" + module
        command = 'mvn -f ' + project_path + ' dependency:tree ' + self.includes_option
        return self.executor.execute(command)

    def __dependencies_to_includes_option(self, dependencies: list[str]) -> str:
        include = ''
        for dependency in dependencies:
            include = include + dependency + ' '
        return '-Dincludes=' + include.strip().replace(' ', ',')
