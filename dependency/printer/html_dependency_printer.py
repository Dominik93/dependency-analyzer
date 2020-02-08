from list_util import maxLength
from ..dependency_matrix import DependencyMatrix
import os


class HtmlDependencyPrinter:

    dependencyMatrix = {}

    def __init__(self, dependencyMatrix: DependencyMatrix):
        self.dependencyMatrix = dependencyMatrix

    def printDependencyMatrix(self):
        f = open("server/dependencies.html", 'w')
        f.write('<table id="modulesTable">\n<tbody>\n')
        f.write(self.__printHeaders())
        f.write(self.__printContent())
        f.write ('</tbody>\n</table>\n')
        f.close()

    def __printHeaders(self):
        dependenciesHeaders = '<tr class="header">\n' + self.__addTag('', 'th' )
        for dependency in self.dependencyMatrix.dependencies:
            dependenciesHeaders += self.__addTag(self.__retriveDependency(dependency), 'th')
        dependenciesHeaders += '</tr>\n'
        return (dependenciesHeaders)
          
    def __printContent(self):
        content = ''
        for module in self.dependencyMatrix.getAllModules():
            content += self.__printRow(module)
        return content

    def __printRow(self, module):
        moduleRow = '<tr>\n' + self.__addTag((module + ' ' + self.dependencyMatrix.getModule(module).version), 'td')
        for dependency in self.dependencyMatrix.dependencies:
            moduleRow += self.__addTag(self.dependencyMatrix.getDependency(module, dependency).version, 'td')
        moduleRow += '</tr>\n'
        return (moduleRow)

    def __addVersion(self, modules):
        modulesWithVersion = []
        for module in modules:
            modulesWithVersion.append(module + ' ' + self.dependencyMatrix.getModule(module).version)
        return modulesWithVersion

    def __addTag(self, string, tag):
        return '<' + tag + '>' + string + '</' + tag + '>\n'
        
    def __retriveDependency(self,string): 
        return string.split(':')[1]