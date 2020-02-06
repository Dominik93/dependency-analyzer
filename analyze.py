import os
from init import modules, dependencies, packages, gitUrl, searchClassUsage, cleanUp, branch, searchDependency, classRegexp
from dependency.dependency_analyzer import DependenciesAnalyzer
from usage.class_usage_analyzer import ClassUsageAnalyzer
from usage.class_usage_printer import printUsageMatrix
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

    if searchClassUsage:
        usageAnalyzer = ClassUsageAnalyzer(modules, packages, classRegexp)
        usageMatrix = usageAnalyzer.calcualteUsage()
        printUsageMatrix(usageMatrix)

finally:    
    if cleanUp:
        removeProjects()
