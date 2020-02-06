import os
from init import modules, dependencies, packages, gitUrl, searchUsage, cleanUp, branch, searchDependency, classRegexp
from dependency.dependency_analyzer import DependenciesAnalyzer
from usage.usage_analyzer import UsageAnalyzer
from matrix_printer import printUsageMatrix
from dependency.dependency_printer import DependencyPriter

def cloneAllProjects():
    for module in modules:
        projectPath = os.getcwd() + '/' + module
        os.popen('git clone ' + gitUrl + '/' + module).read()
        os.popen('git -C '+ projectPath +' checkout ' + branch).read()
        os.popen('git -C '+ projectPath +' pull ').read()

def removeProjects():
    print('Clean up')
    for module in modules:
        projectPath = os.getcwd() + '/' + module
        os.popen('rd /s /q "' + projectPath + '"')

try:
    cloneAllProjects()
   
    if searchDependency:
        dependenciesAnalyzer = DependenciesAnalyzer(modules, dependencies)
        dependencyMatrix = dependenciesAnalyzer.calculateDependencies()
        dependenciesPriter = DependencyPriter(dependencyMatrix)
        dependenciesPriter.printDependencyMatrix()

    if searchUsage:
        usageAnalyzer = UsageAnalyzer(modules, packages, classRegexp)
        usageMatrix = usageAnalyzer.calcualteUsage()
        printUsageMatrix(usageMatrix)

finally:    
    if cleanUp:
        removeProjects()
