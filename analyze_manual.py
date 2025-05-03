from init.init_manual import git_url, branch, modules, dependencies, print_strategy, packages, clean_up, \
    search_class_usage, search_dependency, class_regexp, directory
from analyze import analyze_class_usage, analyze_dependencies, clone_all_projects, remove_projects
from printer_manager import PrinterManager

server_path = "server"

if __name__ == '__main__':
    try:
        clone_all_projects(directory, git_url, branch, modules)
        manager = PrinterManager(print_strategy, server_path)
        if search_dependency:
            dependency_matrix = analyze_dependencies(directory, modules, dependencies)
            manager.set_dependency_matrix(dependency_matrix)
            manager.get_dependency_printer().print()

        if search_class_usage:
            class_usage_matrix = analyze_class_usage(directory, modules, packages, class_regexp)
            manager.set_class_usage_matrix(class_usage_matrix)
            manager.get_class_usage_printer().print()

    finally:
        if clean_up:
            remove_projects(directory, modules)
