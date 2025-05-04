from typing import Callable

from ..dependency_matrix import DependencyMatrix


class HtmlDependencyContentProvider:
    dependency_matrix: DependencyMatrix = {}
    modules_filter: Callable

    def __init__(self, dependency_matrix: DependencyMatrix, element_id=None, modules_filter: Callable = None):
        self.dependency_matrix = dependency_matrix
        self.element_id = element_id
        self.modules_filter = modules_filter if modules_filter is not None else lambda x: True

    def get_content(self):
        content = self.__add_tag(self.__print_headers(), "thead")
        content += self.__add_tag(self.__print_content(), "tbody")
        return self.__add_tag(content, "table", 'class="table" id="' + self.element_id + '"')

    def __print_headers(self):
        dependencies_headers = self.__add_tag('', 'th')
        for dependency in list(filter(lambda x: self._dependency_filter(x), self.dependency_matrix.dependencies)):
            dependencies_headers += self.__add_tag(self.__retrive_dependency(dependency), 'th')
        return self.__add_tag(dependencies_headers, "tr", 'class="header"')

    def __print_content(self):
        content = ''
        for module in self.dependency_matrix.get_modules(self.modules_filter):
            content += self.__print_row(module)
        return content

    def __print_row(self, module):
        module_row = self.__add_tag((module + ' ' + self.dependency_matrix.get_module(module).version), 'th')
        for dependency in list(filter(lambda x: self._dependency_filter(x), self.dependency_matrix.dependencies)):
            module_row += self.__add_tag(self.dependency_matrix.get_dependency(module, dependency).version, 'td')
        return self.__add_tag(module_row, "tr")

    def __add_version(self, modules):
        modules_with_version = []
        for module in modules:
            modules_with_version.append(module + ' ' + self.dependency_matrix.get_module(module).version)
        return modules_with_version

    def _dependency_filter(self, dependency):
        for module in self.dependency_matrix.get_modules(self.modules_filter):
            if self.dependency_matrix.get_module(module).get_dependency(dependency).version != 'unknown':
                return True
        return False

    def __add_tag(self, value, tag, parameters=""):
        return f'<{tag} {parameters}>{value}</{tag}>\n'

    def __retrive_dependency(self, string):
        return string.split(':')[1]
