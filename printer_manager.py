from class_usage.class_usage_matrix import ClassUsageMatrix
from class_usage.printer.html_class_usage_factory import HtmlClassUsageFactory
from class_usage.printer.plain_class_usage_factory import PlainClassUsageFactory
from dependency.dependency_matrix import DependencyMatrix
from printer.console_dependency_printer import ConsoleDependencyPrinter
from printer.file_dependency_printer import FileDependencyPrinter
from dependency.printer.plain_dependency_factory import PlainDependencyFactory
from dependency.printer.html_dependency_factory import HtmlDependencyFactory


class PrinterManager:
    dependency_printer = {}

    class_usage_printer = {}

    def __init__(self, print_strategy: str, server_path: str):
        self.print_strategy = print_strategy
        self.server_path = server_path

    def set_class_usage_matrix(self, class_usage_matrix: ClassUsageMatrix):
        if self.print_strategy == 'html':
            factory = HtmlClassUsageFactory(class_usage_matrix)
            self.class_usage_printer = FileDependencyPrinter(factory.print_class_usage_matrix(), self.server_path,
                                                             "class_usages.html")
        else:
            factory = PlainClassUsageFactory(class_usage_matrix)
            self.class_usage_printer = ConsoleDependencyPrinter(factory.print_class_usage_matrix())

    def set_dependency_matrix(self, dependency_matrix: DependencyMatrix):
        if self.print_strategy == 'html':
            factory = HtmlDependencyFactory(dependency_matrix)
            self.dependency_printer = FileDependencyPrinter(factory.print_dependency_matrix(), self.server_path,
                                                            "dependencies.html")
        else:
            factory = PlainDependencyFactory(dependency_matrix)
            self.dependency_printer = ConsoleDependencyPrinter(factory.print_dependency_matrix())

    def get_class_usage_printer(self):
        return self.class_usage_printer

    def get_dependency_printer(self):
        return self.dependency_printer
