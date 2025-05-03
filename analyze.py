import os

from class_usage.class_usage_analyzer import ClassUsageAnalyzer
from class_usage.class_usage_matrix import ClassUsageMatrix
from dependency.dependency_analyzer import DependenciesAnalyzer
from dependency.dependency_matrix import DependencyMatrix
from dependency.os_executor import OsExecutor
from maven.maven import Maven
from printer_manager import PrinterManager


def clone_all_projects(directory: str, git_url: str, branch: str, modules: list[str]) -> None:
    print(f'Initialize projects')
    for module in modules:
        project_path = directory + '/' + module
        clone_command = 'git clone ' + git_url + '/' + module + ' ' + project_path
        checkout_command = 'git -C ' + project_path + ' checkout ' + branch
        pull_command = 'git -C ' + project_path + ' pull '
        current_branch_command = 'git -C ' + project_path + ' branch --show-current '
        print(f'Execute {clone_command}')
        os.popen(clone_command).read()
        print(f'Execute {current_branch_command}')
        current_branch = os.popen(current_branch_command).read()
        print(f'Current branch {current_branch}')
        if current_branch == branch:
            print(f'Execute {checkout_command}')
            os.popen(checkout_command).read()
            print(f'Execute {pull_command}')
            os.popen(pull_command).read()
    print(f'Projects initialized')


def remove_projects(directory: str, modules: list[str]) -> None:
    print('Clean up')
    for module in modules:
        project_path = directory + '/' + module
        os.popen('rd /s /q "' + project_path + '"')


def analyze_dependencies(directory: str, modules: list[str], dependencies: list[str]) -> DependencyMatrix:
    maven = Maven(directory, OsExecutor(), dependencies)
    dependencies_analyzer = DependenciesAnalyzer(maven, modules, dependencies)
    return dependencies_analyzer.calculate_dependencies(directory)


def analyze_class_usage(directory: str, modules: list[str], packages: list[str], class_regexp: str) -> ClassUsageMatrix:
    class_usage_analyzer = ClassUsageAnalyzer(modules, packages, class_regexp)
    return class_usage_analyzer.calculate_class_usage(directory)
