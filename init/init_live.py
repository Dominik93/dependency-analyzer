import argparse
import configparser

from init.configuration import Configuration, GitConfiguration, AnalyzeConfiguration, ServerConfiguration, \
    ProjectConfiguration

_SEARCH_DEPENDENCY = True

_SEARCH_CLASS_USAGE = True


def _get_modules(config):
    return list(map(str.strip, config['MODULES']['modules'].split(',')))


def _get_dependencies(config):
    return list(map(str.strip, config['DEPENDENCY']['dependencies'].split(',')))


def _get_packages(config):
    return list(map(str.strip, config['USAGE']['packages'].split(',')))

def init():
    parser = argparse.ArgumentParser(description='Live server for analyze dependencies')
    parser.add_argument("--config-file", help='Configuration file, default config.ini', default='config.ini')
    parser.add_argument("--host", help='Host', default='')
    parser.add_argument("--port", help='Port', default=8080)
    parser.add_argument("--interval", help='Interval', default=30)

    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config_file)

    git_configuration = GitConfiguration(config['GIT']['url'], config['GIT']['branch'])
    analyze_configuration = AnalyzeConfiguration(_get_modules(config), _SEARCH_DEPENDENCY, _get_dependencies(config),
                                                 _SEARCH_CLASS_USAGE, _get_packages(config), config['USAGE']['class_regexp'])
    server_configuration = ServerConfiguration(args.host, int(args.port))
    project_configuration = ProjectConfiguration(False, config['DIRECTORY']['directory'])
    configuration = Configuration(git_configuration, analyze_configuration, server_configuration, project_configuration,
                                  'html', int(args.interval))

    print(f"Server configuration {server_configuration} interval: {configuration.interval_in_minutes}")
    print(f"Git configuration {git_configuration}")
    print(f"Analyzing configuration {analyze_configuration}")
    return configuration
