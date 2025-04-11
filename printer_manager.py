from class_usage.printer.html_class_usage_printer import HtmlClassUsagePrinter
from class_usage.printer.console_class_usage_printer import ConsoleClassUsagePrinter
from dependency.printer.console_dependency_printer import ConsoleDependencyPrinter
from dependency.printer.file_dependency_printer import FileDependencyPrinter
from dependency.printer.plain_dependency_factory import PlainDependencyFactory
from dependency.printer.html_dependency_factory import HtmlDependencyFactory


class PrinterManager:
    dependency_printer = {}

    class_usage_printer = {}

    def __init__(self, print_strategy, server_path):
        self.print_strategy = print_strategy
        self.server_path = server_path

    def set_class_usage_matrix(self, class_usage_matrix):
        if self.print_strategy == 'html':
            self.class_usage_printer = HtmlClassUsagePrinter(class_usage_matrix)
        else:
            self.class_usage_printer = ConsoleClassUsagePrinter(class_usage_matrix)

    def set_dependency_matrix(self, dependency_matrix):
        if self.print_strategy == 'html':
            factory = HtmlDependencyFactory(dependency_matrix)
            self.dependency_printer = FileDependencyPrinter(factory.print_dependency_matrix(), self.server_path)
        else:
            dependency_factory = PlainDependencyFactory(dependency_matrix)
            self.dependency_printer = ConsoleDependencyPrinter(dependency_factory.print_dependency_matrix())

    def get_class_usage_printer(self):
        return self.class_usage_printer

    def get_dependency_printer(self):
        return self.dependency_printer
