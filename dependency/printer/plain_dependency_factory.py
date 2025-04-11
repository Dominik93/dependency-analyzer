from ..dependency_matrix import DependencyMatrix


class PlainDependencyFactory:
    SEPARATOR: str = '  |  '
    ROW_SEPARATOR: str = '-----'

    def __init__(self, dependency_matrix: DependencyMatrix):
        self.dependency_matrix = dependency_matrix
        modules_with_version = self.__add_version(self.dependency_matrix.get_all_modules())
        self.module_width = len(max(modules_with_version, key=len))
        self.dependency_width = len(max(map(self.__retrieve_dependency, self.dependency_matrix.dependencies), key=len))
        self.content = ""

    def print_dependency_matrix(self) -> str:
        self.content = 'Dependency matrix:\n'
        self.content += self.__print_headers() + "\n"
        self.content += self.__print_row_separator() + "\n"
        self.content += self.__print_content() + "\n"
        self.content += self.__print_row_separator()
        return self.content

    def __retrieve_dependency(self, string) -> str:
        return string.split(':')[1]

    def __print_row_separator(self) -> str:
        row_separator = ''.ljust(self.module_width, '-') + self.ROW_SEPARATOR
        size = len(self.dependency_matrix.dependencies)
        i = 0
        while i < size:
            row_separator += ''.ljust(self.dependency_width, '-') + self.ROW_SEPARATOR
            i += 1
        return row_separator

    def __print_headers(self) -> str:
        dependencies_headers = ''.ljust(self.module_width, ' ') + self.SEPARATOR
        for dependency in self.dependency_matrix.dependencies:
            retrieve_dependency = self.__retrieve_dependency(dependency)
            dependencies_headers += retrieve_dependency.ljust(self.dependency_width, ' ') + self.SEPARATOR
        return dependencies_headers

    def __print_content(self) -> str:
        contents = []
        for module in self.dependency_matrix.get_all_modules():
            contents.append(self.__print_row(module))
        return "\n".join(contents)

    def __print_row(self, module) -> str:
        module_row = (module + ' ' + self.dependency_matrix.get_module(module).version).ljust(self.module_width, ' ')
        module_row += self.SEPARATOR
        for dependency_name in self.dependency_matrix.dependencies:
            dependency = self.dependency_matrix.get_dependency(module, dependency_name)
            module_row += dependency.version.ljust(self.dependency_width, ' ')
            module_row += self.SEPARATOR
        return module_row

    def __max_length(self, array) -> int:
        length = 0
        for item in array:
            if len(item) > length:
                length = len(item)
        return length

    def __add_version(self, modules) -> list[str]:
        modules_with_version = []
        for module in modules:
            modules_with_version.append(module + ' ' + self.dependency_matrix.get_module(module).version)
        return modules_with_version
