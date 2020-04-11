import os


class HtmlDependencyPrinter:

    dependencyMatrix = {}

    def __init__(self, dependencyMatrix, modules, dependencies):
        self.dependencyMatrix = dependencyMatrix
        self.modules = modules
        self.dependencies = dependencies

    def printDependencyMatrix(self):
        f = open("server/dependencies.html", 'w')
        f.write('<table id="modulesTable">\n<tbody>\n')
        f.write(self.__printHeaders())
        f.write(self.__printContent())
        f.write ('</tbody>\n</table>\n')
        f.close()

    def __printHeaders(self):
        dependenciesHeaders = '<tr class="header">\n' + self.__addTag('', 'th' )
        for dependency in self.dependencies.get():
            dependenciesHeaders += self.__addTag(dependency.artifactId + ":" + dependency.version, 'th')
        dependenciesHeaders += '</tr>\n'
        return (dependenciesHeaders)
          
    def __printContent(self):
        content = ''
        for module in self.modules.get():
            content += self.__printRow(module)
        return content

    def __printRow(self, module):
        moduleRow = '<tr>\n' + self.__addTag(module.name + ':' + module.version, 'td')
        for dependency in self.dependencies.get():
            moduleRow += self.__addTag(self.dependencyMatrix[module.name][dependency.artifactId], 'td')
        moduleRow += '</tr>\n'
        return (moduleRow)

    def __addTag(self, string, tag):
        return '<' + tag + '>' + string + '</' + tag + '>\n'
        