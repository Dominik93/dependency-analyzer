import os
from class_usage.class_usage_analyzer import ClassUsageAnalyzer
from class_usage.printer.console_class_usage_printer import ConsoleClassUsagePrinter
from class_usage.printer.html_class_usage_printer import HtmlClassUsagePrinter
from dependency.dependency_analyzer import DependenciesAnalyzer
from dependency.printer.console_dependency_printer import ConsoleDependencyPrinter
from dependency.printer.html_dependency_printer import HtmlDependencyPrinter
from printer_manager import PrinterManager

def cloneAllProjects(gitUrl, branch, modules):
    for module in modules:
        projectPath = os.getcwd() + '/temp/' + module
        os.popen('git clone ' + gitUrl + '/' + module +' temp/' + module).read()
        os.popen('git -C '+ projectPath +' checkout ' + branch).read()
        os.popen('git -C '+ projectPath +' pull ').read()

def removeProjects(modules):
    print('Clean up')
    for module in modules:
        projectPath = os.getcwd() + '/temp/' + module
        os.popen('rd /s /q "' + projectPath + '"')


def analyzeDependencies(modules, dependencies, printStrategy):
    dependenciesAnalyzer = DependenciesAnalyzer(modules, dependencies)
    dependencyMatrix = dependenciesAnalyzer.calculateDependencies()
    manager = PrinterManager(printStrategy)
    manager.setDependnecyMatrix(dependencyMatrix)
    manager.getDependencyPrinter().printDependencyMatrix()

def analyzeClassUsage(modules, packages, classRegexp, printStrategy):  
    classUsageAnalyzer = ClassUsageAnalyzer(modules, packages, classRegexp)
    classUsageMatrix = classUsageAnalyzer.calcualteClassUsage()
    manager = PrinterManager(printStrategy)
    manager.setClassUsageMatrix(classUsageMatrix)
    manager.getClassUsagePrinter().printClassUsageMatrix()

