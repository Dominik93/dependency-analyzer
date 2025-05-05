import argparse
import configparser

from init.configuration import Configuration, AnalyzeConfiguration, GitConfiguration, \
    ProjectConfiguration


def _get_modules():
    return list(map(str.strip, config['MODULES']['modules'].split(','))) if len(
        args.only_include_modules) == 0 else list(
        map(str.strip, args.only_include_modules.split(',')))


def _get_dependencies():
    return list(map(str.strip, config['DEPENDENCY']['dependencies'].split(','))) if len(
        args.only_include_dependencies) == 0 else list(map(str.strip, args.only_include_dependencies.split(',')))


def _get_packages():
    return list(map(str.strip, config['USAGE']['packages'].split(',')))

def init():
    parser = argparse.ArgumentParser(description='Tool for analyze dependencies')
    parser.add_argument("--config-file", help='Configuration file, default config.ini', default='config.ini')
    parser.add_argument("--only-include-modules", help='Ignore modules in config and use only this', default='')
    parser.add_argument("--search-dependencies", help='Search for dependency in modules', action='store_true')
    parser.add_argument("--only-include-dependencies", help='Ignore dependencies in config and use only this', default='')
    parser.add_argument("--search-class-usage", help='Serac form class usage in modules', action='store_true')
    parser.add_argument("--no-clean-up", help='Remove all projects', action='store_false')
    parser.add_argument("--print", choices=['console', 'html'], help='Strategy of printing', default='console')
    parser.add_argument("--directory", help='Directory where modules will be cloned', default='')

    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config_file)

    git_configuration = GitConfiguration(config['GIT']['url'], config['GIT']['branch'])
    analyze_configuration = AnalyzeConfiguration(_get_modules(), args.search_dependencies, _get_dependencies(),
                                                 args.search_class_usage, _get_packages(), config['USAGE']['class_regexp'])
    server_configuration = None
    project_configuration = ProjectConfiguration(args.no_clean_up, config['DIRECTORY']['directory'])
    configuration = Configuration(git_configuration, analyze_configuration, server_configuration, project_configuration,
                                  args.print, int(args.interval))

    print(f"Git configuration {git_configuration}")
    print(f"Analyzing configuration {analyze_configuration}")
    return configuration
