from init.init_manual import gitUrl, branch, modules, dependencies, print_strategy, packages, cleanUp, searchClassUsage, \
    searchDependency, class_regexp
from analyze import analyze_class_usage, analyze_dependencies, clone_all_projects, remove_projects

try:
    clone_all_projects(gitUrl, branch, modules)
    if searchDependency:
        analyze_dependencies(modules, dependencies, print_strategy)

    if searchClassUsage:
        analyze_class_usage(modules, packages, class_regexp, print_strategy)

finally:
    if cleanUp:
        remove_projects(modules)
