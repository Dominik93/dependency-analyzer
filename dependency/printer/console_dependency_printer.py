from ..dependency_matrix import DependencyMatrix


class ConsoleDependencyPrinter:
    SEPARATOR = '  |  '
    ROW_SEPARATOR = '-----'
    dependency_matrix = {}

    module_width = 0
    dependency_width = 0

    def __init__(self, dependency_matrix: DependencyMatrix):
        self.dependency_matrix = dependency_matrix
        modules_with_version = self.__add_version(self.dependency_matrix.get_all_modules())
        self.module_width = len(max(modules_with_version, key=len))
        self.dependency_width = len(max(map(self.__retrive_dependency, self.dependency_matrix.dependencies), key=len))

    def print_dependency_matrix(self):
        print('Dependency matrix:')
        self.__print_headers()
        self.__print_row_separator()
        self.__print_content()
        self.__print_row_separator()

    def __retrive_dependency(self, string):
        return string.split(':')[1]

    def __print_row_separator(self):
        row_separator = ''.ljust(self.module_width, '-') + self.ROW_SEPARATOR
        size = len(self.dependency_matrix.dependencies)
        i = 0
        while i < size:
            row_separator += ''.ljust(self.dependency_width, '-') + self.ROW_SEPARATOR
            i += 1
        print(row_separator)

    def __print_headers(self):
        dependencies_headers = ''.ljust(self.module_width, ' ') + self.SEPARATOR
        for dependency in self.dependency_matrix.dependencies:
            dependencies_headers += self.__retrive_dependency(dependency).ljust(self.dependency_width,
                                                                                ' ') + self.SEPARATOR
        print(dependencies_headers)

    def __print_content(self):
        for module in self.dependency_matrix.get_all_modules():
            self.__print_row(module)

    def __print_row(self, module):
        module_row = (module + ' ' + self.dependency_matrix.get_module(module).version).ljust(self.module_width,
                                                                                              '.') + self.SEPARATOR
        for dependency in self.dependency_matrix.dependencies:
            module_row += self.dependency_matrix.get_dependency(module, dependency).version.ljust(self.dependency_width,
                                                                                                  ' ') + self.SEPARATOR
        print(module_row)

    def __max_length(self, array):
        length = 0
        for item in array:
            if len(item) > length:
                length = len(item)
        return length

    def __add_version(self, modules):
        modules_with_version = []
        for module in modules:
            modules_with_version.append(module + ' ' + self.dependency_matrix.get_module(module).version)
        return modules_with_version
