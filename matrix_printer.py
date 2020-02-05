from init import modules, dependencies, packages
from list_util import maxLength

SEPARATOR = '  |  '

def retriveDependency(string): 
    return string.split(':')[1]

def printSeparator(dependencyMatrix):
    modulesWithVersion = addVersion(dependencyMatrix, modules)
    modulesWidth = maxLength(modulesWithVersion)
    dependenciesWidth = maxLength(map(retriveDependency, dependencies)) 
    separator = ''.ljust(modulesWidth, '-') + '-----'
    for dependency in dependencies:
        separator += ''.ljust(dependenciesWidth, '-') + '-----'
    print(separator)

def printHeaders(dependencyMatrix):
    dependenciesWidth = maxLength(map(retriveDependency, dependencies)) 
    modulesWithVersion = addVersion(dependencyMatrix, modules)
    modulesWidth = maxLength(modulesWithVersion)
    dependenciesHeaders = ''.ljust(modulesWidth, ' ') + SEPARATOR
    for dependency in dependencies:
        dependenciesHeaders += retriveDependency(dependency).ljust(dependenciesWidth, ' ') + SEPARATOR
    print(dependenciesHeaders)
    
def printRow(dependencyMatrix, module, modulesWidth):
    dependenciesWidth = maxLength(map(retriveDependency, dependencies))
    moduleRow = (module + ' ' + dependencyMatrix[module]['_version']).ljust(modulesWidth, '.') + SEPARATOR
    for dependency in dependencies:
        moduleRow += dependencyMatrix[module][dependency].ljust(dependenciesWidth, ' ') + SEPARATOR
    print(moduleRow)

def addVersion(dependencyMatrix, modules):
    modulesWithVersion = []
    for module in modules:
        modulesWithVersion.append(module + ' ' + dependencyMatrix[module]['_version'])
    return modulesWithVersion

def printContent(dependencyMatrix):
    modulesWithVersion = addVersion(dependencyMatrix, modules)
    modulesWidth = maxLength(modulesWithVersion)
    for module in modules:
        printRow(dependencyMatrix, module, modulesWidth)

def printDependencyMatrix(dependencyMatrix):
    print('Dependency matrix:')
    printHeaders(dependencyMatrix)
    printSeparator(dependencyMatrix)
    printContent(dependencyMatrix)
    printSeparator(dependencyMatrix)
   

def printUsageMatrix(usageMatrix):
    print('Usage matrix:')
    for module in usageMatrix.keys():
        print('Module: ' + module)	
        for dependency in usageMatrix[module].keys():
            if len(usageMatrix[module][dependency]) > 0:
                print('Dependency:' + dependency)
                for item in usageMatrix[module][dependency]:
                    print('\t' + str(item))
