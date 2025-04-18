from ..class_usage_matrix import ClassUsageMatrix


class HtmlClassUsageFactory:
    class_usage_matrix: ClassUsageMatrix = {}
    content = ""

    def __init__(self, class_usage_matrix: ClassUsageMatrix):
        self.class_usage_matrix = class_usage_matrix

    def print_class_usage_matrix(self):
        self.content = ""
        self.content += '<table id="classUsagesTable">\n<tbody>\n'
        self.content += self.__print_headers()
        self.content += self.__print_content()
        self.content += '</tbody>\n</table>\n'
        return self.content

    def __print_headers(self):
        dependencies_headers = '<tr class="header">\n' + self.__add_tag('', 'th')
        for dependency in self.class_usage_matrix.dependencies:
            dependencies_headers += self.__add_tag(self.__retrive_dependency(dependency), 'th')
        dependencies_headers += '</tr>\n'
        return dependencies_headers

    def __print_content(self):
        content = ''
        for module in self.class_usage_matrix.get_all_modules():
            content += self.__print_row(module)
        return content

    def __print_row(self, module):
        version = module + ' ' + self.class_usage_matrix.get_module(module).version
        module_row = '<tr>\n' + self.__add_tag(version, 'td')
        for dependency in self.class_usage_matrix.dependencies:
            module_row += self.__add_tag(
                self.__classes_to_html(self.class_usage_matrix.get_dependency(module, dependency).classes), 'td')
        module_row += '</tr>\n'
        return module_row

    def __add_version(self, modules):
        modules_with_version = []
        for module in modules:
            modules_with_version.append(module + ' ' + self.class_usage_matrix.get_module(module).version)
        return modules_with_version

    def __add_tag(self, string, tag):
        return '<' + tag + '>' + string + '</' + tag + '>\n'

    def __retrive_dependency(self, string):
        return string.split(':')[0]

    def __classes_to_html(self, classes):
        content = ''
        for a_class in classes:
            content += a_class + '\n'
        return content
