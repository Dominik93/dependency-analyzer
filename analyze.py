import os
from init import modules, dependencies, packages, gitUrl, searchUsage, cleanUp, branch
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

dependenciesAnalyzer = DependenciesAnalyzer(modules, dependencies)
usageAnalyzer = UsageAnalyzer(modules, packages)

try:
    cloneAllProjects()
    dependencyMatrix = dependenciesAnalyzer.calculateDependencies()
    dependenciesPriter = DependencyPriter(dependencyMatrix)
    dependenciesPriter.printDependencyMatrix()

    if searchUsage:
        usageMatrix = usageAnalyzer.calcualteUsage()
        printUsageMatrix(usageMatrix)

finally:    
    if cleanUp:
        removeProjects()
