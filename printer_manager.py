from class_usage.printer.html_class_usage_printer import HtmlClassUsagePrinter
from class_usage.printer.console_class_usage_printer import ConsoleClassUsagePrinter
from dependency.printer.console_dependency_printer import ConsoleDependencyPrinter
from dependency.printer.html_dependency_printer import HtmlDependencyPrinter

class PrinterManager:

    printStrategy = ''

    dependencyPrinter = {}

    classUsagePrinter = {}

    def __init__(self, printStrategy):
        self.printStrategy = printStrategy

    def setClassUsageMatrix(self, classUsageMatrix):
        if self.printStrategy == 'html':
            self.classUsagePrinter = HtmlClassUsagePrinter(classUsageMatrix)
        else:
            self.classUsagePrinter = ConsoleClassUsagePrinter(classUsageMatrix)

    def setDependnecyMatrix(self, dependencyMatrix):
        if self.printStrategy == 'html':
            self.dependencyPrinter = HtmlDependencyPrinter(dependencyMatrix)
        else:
            self.dependencyPrinter = ConsoleDependencyPrinter(dependencyMatrix)

    def getClassUsagePrinter(self):
        return self.classUsagePrinter

    def getDependencyPrinter(self):
        return self.dependencyPrinter