from init.init_manual import git_url, branch, modules, dependencies, print_strategy, packages, clean_up, search_class_usage, \
    search_dependency, class_regexp
from analyze import analyze_class_usage, analyze_dependencies, clone_all_projects, remove_projects


if __name__ == '__main__':
    try:
        clone_all_projects(git_url, branch, modules)
        if search_dependency:
            analyze_dependencies('server/', modules, dependencies, print_strategy)

        if search_class_usage:
            analyze_class_usage('server/', modules, packages, class_regexp, print_strategy)

    finally:
        if clean_up:
            remove_projects(modules)
