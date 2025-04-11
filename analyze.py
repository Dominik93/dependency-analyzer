import os
from class_usage.class_usage_analyzer import ClassUsageAnalyzer
from dependency.dependency_analyzer import DependenciesAnalyzer
from dependency.os_executor import OsExecutor
from maven.maven import Maven
from printer_manager import PrinterManager


def clone_all_projects(git_url, branch, modules):
    for module in modules:
        project_path = os.getcwd() + '/temp/' + module
        os.popen('git clone ' + git_url + '/' + module + ' temp/' + module).read()
        os.popen('git -C ' + project_path + ' checkout ' + branch).read()
        os.popen('git -C ' + project_path + ' pull ').read()


def remove_projects(modules):
    print('Clean up')
    for module in modules:
        project_path = os.getcwd() + '/temp/' + module
        os.popen('rd /s /q "' + project_path + '"')


def analyze_dependencies(server_path, modules, dependencies, prints_strategy):
    maven = Maven(OsExecutor(), dependencies)
    dependencies_analyzer = DependenciesAnalyzer(maven, modules, dependencies)
    dependency_matrix = dependencies_analyzer.calculate_dependencies()
    manager = PrinterManager(prints_strategy, server_path)
    manager.set_dependency_matrix(dependency_matrix)
    manager.get_dependency_printer().print()


def analyze_class_usage(server_path, modules, packages, class_regexp, print_strategy):
    maven = Maven(OsExecutor(), [])
    class_usage_analyzer = ClassUsageAnalyzer(maven, modules, packages, class_regexp)
    class_usage_matrix = class_usage_analyzer.calculate_class_usage()
    manager = PrinterManager(print_strategy, server_path)
    manager.set_class_usage_matrix(class_usage_matrix)
    manager.get_class_usage_printer().print()
