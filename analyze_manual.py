from init.init_manual import git_url, branch, modules, dependencies, print_strategy, packages, clean_up, \
    search_class_usage, search_dependency, class_regexp, directory
from analyze import analyze_class_usage, analyze_dependencies, clone_all_projects, remove_projects

server_path = "server"

if __name__ == '__main__':
    try:
        clone_all_projects(directory, git_url, branch, modules)
        if search_dependency:
            analyze_dependencies(directory, server_path, modules, dependencies, print_strategy)

        if search_class_usage:
            analyze_class_usage(directory, server_path, modules, packages, class_regexp, print_strategy)

    finally:
        if clean_up:
            remove_projects(directory, modules)
