from init import *
from list_util import maxLength

SEPARATOR = '  |  '

def retriveDependency(string): 
    return string.split(':')[1]

def fillWith(string, width, fill = '.'):
    return string.ljust(width, fill)

def printSeparator():
    dependenciesWidth = maxLength(map(retriveDependency, dependencies)) 
    separator = fillWith('', dependenciesWidth, '-') + '-----'
    for dependency in dependencies:
        separator += fillWith('', dependenciesWidth, '-') + '-----'
    print(separator)

def printHeaders():
    dependenciesWidth = maxLength(map(retriveDependency, dependencies)) 
    modulesWidth = maxLength(modules)
    dependenciesHeaders = fillWith('', modulesWidth, ' ') + SEPARATOR
    for dependency in dependencies:
        dependenciesHeaders += fillWith(retriveDependency(dependency), dependenciesWidth, ' ') + SEPARATOR
    print(dependenciesHeaders)
    
def printRow(dependencyMatrix, module, modulesWidth):
    dependenciesWidth = maxLength(map(retriveDependency, dependencies))
    moduleRow = fillWith(module, modulesWidth, '.') + SEPARATOR
    for dependency in dependencies:
        moduleRow += fillWith(dependencyMatrix[module][dependency], dependenciesWidth, ' ') + SEPARATOR
    print(moduleRow)

def printContent(dependencyMatrix):
    modulesWidth = maxLength(modules)
    for module in modules:
        printRow(dependencyMatrix, module, modulesWidth)

def printDependencyMatrix(dependencyMatrix):
    print('Dependency matrix:')
    printHeaders()
    printSeparator()
    printContent(dependencyMatrix)
   

