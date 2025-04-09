from class_usage.printer.html_class_usage_printer import HtmlClassUsagePrinter
from class_usage.printer.console_class_usage_printer import ConsoleClassUsagePrinter
from dependency.printer.console_dependency_printer import ConsoleDependencyPrinter
from dependency.printer.html_dependency_printer import HtmlDependencyPrinter


class PrinterManager:
    print_strategy = ''

    dependency_printer = {}

    class_usage_printer = {}

    def __init__(self, print_strategy):
        self.print_strategy = print_strategy

    def set_class_usage_matrix(self, class_usage_matrix):
        if self.print_strategy == 'html':
            self.class_usage_printer = HtmlClassUsagePrinter(class_usage_matrix)
        else:
            self.class_usage_printer = ConsoleClassUsagePrinter(class_usage_matrix)

    def set_dependency_matrix(self, dependency_matrix):
        if self.print_strategy == 'html':
            self.dependency_printer = HtmlDependencyPrinter(dependency_matrix)
        else:
            self.dependency_printer = ConsoleDependencyPrinter(dependency_matrix)

    def get_class_usage_printer(self):
        return self.class_usage_printer

    def get_dependency_printer(self):
        return self.dependency_printer
