import os
from init import modules, dependencies, packages, gitUrl, searchUsage, cleanUp, branch
from dependency_analyzer import DependenciesAnalyzer
from usage_analyzer import UsageAnalyzer
from matrix_printer import printDependencyMatrix, printUsageMatrix

def cloneAllProjects():
    print('Clone modules: ' + str(modules))
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
    printDependencyMatrix(dependencyMatrix)

    if searchUsage:
        usageMatrix = usageAnalyzer.calcualteUsage()
        printUsageMatrix(usageMatrix)

finally:    
    if cleanUp:
        removeProjects()
