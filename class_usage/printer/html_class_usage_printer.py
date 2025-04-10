from ..class_usage_matrix import ClassUsageMatrix
import os


class HtmlClassUsagePrinter:
    class_usage_matrix: ClassUsageMatrix = {}

    def __init__(self, class_usage_matrix: ClassUsageMatrix):
        self.class_usage_matrix = class_usage_matrix

    def print_class_usage_matrix(self):
        f = open("server/class_usages.html", 'w')
        f.write('<table id="classUsagesTable">\n<tbody>\n')
        f.write(self.__print_headers())
        f.write(self.__print_content())
        f.write('</tbody>\n</table>\n')
        f.close()

    def __print_headers(self):
        dependenciesHeaders = '<tr class="header">\n' + self.__add_tag('', 'th')
        for dependency in self.class_usage_matrix.dependencies:
            dependenciesHeaders += self.__add_tag(self.__retrive_dependency(dependency), 'th')
        dependenciesHeaders += '</tr>\n'
        return (dependenciesHeaders)

    def __print_content(self):
        content = ''
        for module in self.class_usage_matrix.get_all_modules():
            content += self.__print_row(module)
        return content

    def __print_row(self, module):
        moduleRow = '<tr>\n' + self.__add_tag((module + ' ' + self.class_usage_matrix.get_module(module).version), 'td')
        for dependency in self.class_usage_matrix.dependencies:
            moduleRow += self.__add_tag(
                self.__classes_to_html(self.class_usage_matrix.get_dependency(module, dependency).classes), 'td')
        moduleRow += '</tr>\n'
        return (moduleRow)

    def __add_version(self, modules):
        modulesWithVersion = []
        for module in modules:
            modulesWithVersion.append(module + ' ' + self.class_usage_matrix.get_module(module).version)
        return modulesWithVersion

    def __add_tag(self, string, tag):
        return '<' + tag + '>' + string + '</' + tag + '>\n'

    def __retrive_dependency(self, string):
        return string.split(':')[0]

    def __classes_to_html(self, classes):
        content = ''
        for aClass in classes:
            content += aClass + '\n'
        return content
