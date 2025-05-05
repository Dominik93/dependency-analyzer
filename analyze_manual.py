from analyze import analyze_class_usage, analyze_dependencies, clone_all_projects, remove_projects
from init.init_manual import init
from printer_manager import PrinterManager

server_path = "server"

if __name__ == '__main__':
    configuration = init()
    server_configuration = configuration.server_configuration
    git_configuration = configuration.git_configuration
    project_configuration = configuration.project_configuration
    analyze_configuration = configuration.analyze_configuration
    try:
        clone_all_projects(project_configuration.directory, git_configuration.git_url, git_configuration.branch,
                           analyze_configuration.modules)
        manager = PrinterManager(configuration.print_strategy, server_path)
        if analyze_configuration.search_dependency:
            dependency_matrix = analyze_dependencies(project_configuration.directory, analyze_configuration.modules,
                                                     analyze_configuration.dependencies)
            manager.set_dependency_matrix(dependency_matrix)
            manager.get_dependency_printer().print()

        if analyze_configuration.search_class_usage:
            class_usage_matrix = analyze_class_usage(project_configuration.directory, analyze_configuration.modules,
                                                     analyze_configuration.packages, analyze_configuration.class_regexp)
            manager.set_class_usage_matrix(class_usage_matrix)
            manager.get_class_usage_printer().print()

    finally:
        if project_configuration.clean_up:
            remove_projects(project_configuration.directory, analyze_configuration.modules)
