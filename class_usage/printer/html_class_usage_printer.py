from ..class_usage_matrix import ClassUsageMatrix
import os


class HtmlClassUsagePrinter:
    class_usage_matrix: ClassUsageMatrix = {}

    def __init__(self, class_usage_matrix: ClassUsageMatrix):
        self.class_usage_matrix = class_usage_matrix

    def printClassUsageMatrix(self):
        f = open("server/class_usages.html", 'w')
        f.write('<table id="classUsagesTable">\n<tbody>\n')
        f.write(self.__printHeaders())
        f.write(self.__printContent())
        f.write('</tbody>\n</table>\n')
        f.close()

    def __printHeaders(self):
        dependenciesHeaders = '<tr class="header">\n' + self.__addTag('', 'th')
        for dependency in self.class_usage_matrix.dependencies:
            dependenciesHeaders += self.__addTag(self.__retriveDependency(dependency), 'th')
        dependenciesHeaders += '</tr>\n'
        return (dependenciesHeaders)

    def __printContent(self):
        content = ''
        for module in self.class_usage_matrix.get_all_modules():
            content += self.__printRow(module)
        return content

    def __printRow(self, module):
        moduleRow = '<tr>\n' + self.__addTag((module + ' ' + self.class_usage_matrix.get_module(module).version), 'td')
        for dependency in self.class_usage_matrix.dependencies:
            moduleRow += self.__addTag(
                self.__classesToHtml(self.class_usage_matrix.get_dependency(module, dependency).classes), 'td')
        moduleRow += '</tr>\n'
        return (moduleRow)

    def __addVersion(self, modules):
        modulesWithVersion = []
        for module in modules:
            modulesWithVersion.append(module + ' ' + self.class_usage_matrix.get_module(module).version)
        return modulesWithVersion

    def __addTag(self, string, tag):
        return '<' + tag + '>' + string + '</' + tag + '>\n'

    def __retriveDependency(self, string):
        return string.split(':')[0]

    def __classesToHtml(self, classes):
        content = ''
        for aClass in classes:
            content += aClass + '\n'
        return content
