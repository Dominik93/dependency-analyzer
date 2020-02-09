from ..class_usage_matrix import ClassUsageMatrix
import os


class HtmlClassUsagePrinter:

    classUsageMatrix: ClassUsageMatrix = {}

    def __init__(self, classUsageMatrix: ClassUsageMatrix):
        self.classUsageMatrix = classUsageMatrix

    def printClassUsageMatrix(self):
        f = open("server/class_usages.html", 'w')
        f.write('<table id="classUsagesTable">\n<tbody>\n')
        f.write(self.__printHeaders())
        f.write(self.__printContent())
        f.write ('</tbody>\n</table>\n')
        f.close()

    def __printHeaders(self):
        dependenciesHeaders = '<tr class="header">\n' + self.__addTag('', 'th' )
        for dependency in self.classUsageMatrix.dependencies:
            dependenciesHeaders += self.__addTag(self.__retriveDependency(dependency), 'th')
        dependenciesHeaders += '</tr>\n'
        return (dependenciesHeaders)
          
    def __printContent(self):
        content = ''
        for module in self.classUsageMatrix.getAllModules():
            content += self.__printRow(module)
        return content

    def __printRow(self, module):
        moduleRow = '<tr>\n' + self.__addTag((module + ' ' + self.classUsageMatrix.getModule(module).version), 'td')
        for dependency in self.classUsageMatrix.dependencies:
            moduleRow += self.__addTag(self.__classesToHtml(self.classUsageMatrix.getDependency(module, dependency).classes), 'td')
        moduleRow += '</tr>\n'
        return (moduleRow)

    def __addVersion(self, modules):
        modulesWithVersion = []
        for module in modules:
            modulesWithVersion.append(module + ' ' + self.classUsageMatrix.getModule(module).version)
        return modulesWithVersion

    def __addTag(self, string, tag):
        return '<' + tag + '>' + string + '</' + tag + '>\n'
        
    def __retriveDependency(self,string): 
        return string.split(':')[0]

    def __classesToHtml(self, classes):
        content = ''
        for aClass in classes:
            content += aClass + '\n'
        return content