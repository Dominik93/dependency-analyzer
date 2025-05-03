from class_usage.class_usage_matrix import ClassUsageMatrix
from class_usage.content.html_class_usage_content_provider import HtmlClassUsageContentProvider
from class_usage.content.plain_class_usage_content_provider import PlainClassUsageContentProvider
from dependency.dependency_matrix import DependencyMatrix
from modules.content.html_modules_content_provider import HtmlModulesContentProvider
from modules.content.plain_modules_content_provider import PlainModulesContentProvider
from printer.console_printer import ConsolePrinter
from printer.file_printer import FilePrinter
from dependency.content.plain_dependency_content_provider import PlainDependencyContentProvider
from dependency.content.html_dependency_content_provider import HtmlDependencyContentProvider


class PrinterManager:
    dependency_printer = {}

    class_usage_printer = {}

    modules_printer = {}

    def __init__(self, print_strategy: str, server_path: str):
        self.print_strategy = print_strategy
        self.server_path = server_path

    def set_class_usage_matrix(self, class_usage_matrix: ClassUsageMatrix):
        if self.print_strategy == 'html':
            factory = HtmlClassUsageContentProvider(class_usage_matrix)
            self.class_usage_printer = FilePrinter(factory.get_content(), self.server_path, "class_usages.html")
        else:
            factory = PlainClassUsageContentProvider(class_usage_matrix)
            self.class_usage_printer = ConsolePrinter(factory.get_content())

    def set_dependency_matrix(self, dependency_matrix: DependencyMatrix):
        if self.print_strategy == 'html':
            factory = HtmlDependencyContentProvider(dependency_matrix)
            self.dependency_printer = FilePrinter(factory.get_content(), self.server_path, "dependencies.html")
        else:
            factory = PlainDependencyContentProvider(dependency_matrix)
            self.dependency_printer = ConsolePrinter(factory.get_content())

    def set_modules(self, modules: list[str], dependency_matrix: DependencyMatrix,
                    class_usage_matrix: ClassUsageMatrix):
        if self.print_strategy == 'html':
            factory = HtmlModulesContentProvider(modules, dependency_matrix, class_usage_matrix)
            self.modules_printer = FilePrinter(factory.get_content(), self.server_path, "modules.html")
        else:
            factory = PlainModulesContentProvider(modules, dependency_matrix, class_usage_matrix)
            self.modules_printer = ConsolePrinter(factory.get_content())

    def get_class_usage_printer(self):
        return self.class_usage_printer

    def get_modules_printer(self):
        return self.modules_printer

    def get_dependency_printer(self):
        return self.dependency_printer
