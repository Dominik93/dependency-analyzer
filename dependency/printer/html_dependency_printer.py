from ..dependency_matrix import DependencyMatrix


class HtmlDependencyPrinter:
    dependency_matrix = {}

    def __init__(self, dependency_matrix: DependencyMatrix):
        self.dependency_matrix = dependency_matrix

    def print_dependency_matrix(self):
        f = open("server/dependencies.html", 'w')
        f.write('<table id="modulesTable">\n<tbody>\n')
        f.write(self.__print_headers())
        f.write(self.__print_content())
        f.write('</tbody>\n</table>\n')
        f.close()

    def __print_headers(self):
        dependencies_headers = '<tr class="header">\n' + self.__add_tag('', 'th')
        for dependency in self.dependency_matrix.dependencies:
            dependencies_headers += self.__add_tag(self.__retrive_dependency(dependency), 'th')
        dependencies_headers += '</tr>\n'
        return dependencies_headers

    def __print_content(self):
        content = ''
        for module in self.dependency_matrix.get_all_modules():
            content += self.__print_row(module)
        return content

    def __print_row(self, module):
        module_row = '<tr>\n' + self.__add_tag((module + ' ' + self.dependency_matrix.get_module(module).version), 'td')
        for dependency in self.dependency_matrix.dependencies:
            module_row += self.__add_tag(self.dependency_matrix.get_dependency(module, dependency).version, 'td')
        module_row += '</tr>\n'
        return module_row

    def __add_version(self, modules):
        modules_with_version = []
        for module in modules:
            modules_with_version.append(module + ' ' + self.dependency_matrix.get_module(module).version)
        return modules_with_version

    def __add_tag(self, string, tag):
        return '<' + tag + '>' + string + '</' + tag + '>\n'

    def __retrive_dependency(self, string):
        return string.split(':')[1]
