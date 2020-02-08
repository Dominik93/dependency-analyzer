import os
from usage.class_usage_analyzer import ClassUsageAnalyzer
from usage.console_class_usage_printer import ConsoleClassUsagePrinter
from usage.html_class_usage_printer import HtmlClassUsagePrinter
from dependency.dependency_analyzer import DependenciesAnalyzer
from dependency.printer.console_dependency_printer import ConsoleDependencyPrinter
from dependency.printer.html_dependency_printer import HtmlDependencyPrinter

def cloneAllProjects(gitUrl, branch, modules):
    for module in modules:
        projectPath = os.getcwd() + '/' + module
        os.popen('git clone ' + gitUrl + '/' + module).read()
        os.popen('git -C '+ projectPath +' checkout ' + branch).read()
        os.popen('git -C '+ projectPath +' pull ').read()

def removeProjects(modules):
    print('Clean up')
    for module in modules:
        projectPath = os.getcwd() + '/' + module
        os.popen('rd /s /q "' + projectPath + '"')


def analyzeDependencies(modules, dependencies, printStrategy):
    dependenciesAnalyzer = DependenciesAnalyzer(modules, dependencies)
    dependencyMatrix = dependenciesAnalyzer.calculateDependencies()
    if printStrategy == 'html':
        HtmlDependencyPrinter(dependencyMatrix).printDependencyMatrix()
    else:
        ConsoleDependencyPrinter(dependencyMatrix).printDependencyMatrix()

def analyzeClassUsage(modules, packages, classRegexp, printStrategy):  
    usageAnalyzer = ClassUsageAnalyzer(modules, packages, classRegexp)
    usageMatrix = usageAnalyzer.calcualteUsage()
    print(usageMatrix)
    if printStrategy == 'html':
        HtmlClassUsagePrinter(usageMatrix).printUsageMatrix()
    else:
        ConsoleClassUsagePrinter().printUsageMatrix(usageMatrix)

