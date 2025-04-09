import sys
import os
import configparser
import shutil
import argparse

parser = argparse.ArgumentParser(description='Tool for analyze dependencies')
parser.add_argument("--config-file", help='Configuration file, default config.ini', default='config.ini')
parser.add_argument("--only-include-modules", help='Ignore modules in config and use only this', default='')
parser.add_argument("--search-dependencies", help='Search for dependency in modules', action='store_true')
parser.add_argument("--only-include-dependencies", help='Ignore dependencies in config and use only this', default='')
parser.add_argument("--search-class-usage", help='Serac form class usage in modules', action='store_true')
parser.add_argument("--no-clean-up", help='Remove all projects', action='store_false')
parser.add_argument("--print", choices=['console', 'html'], help='Stategy of printing', default='console')

args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config_file)
gitUrl = config['GIT']['url']
branch = config['GIT']['branch']

cleanUp = args.no_clean_up
searchDependency = args.search_dependencies
searchClassUsage = args.search_class_usage

if len(args.only_include_modules) == 0:
    modules = list(map(str.strip, config['MODULES']['modules'].split(',')))
else:
    modules = list(map(str.strip, args.only_include_modules.split(',')))

if len(args.only_include_dependencies) == 0:
    dependencies = list(map(str.strip, config['DEPENDENCY']['dependencies'].split(',')))
else:
    dependencies = list(map(str.strip, args.only_include_dependencies.split(',')))

packages = list(map(str.strip, config['USAGE']['packages'].split(',')))

class_regexp = config['USAGE']['class_regexp']

print_strategy = args.print

print(dependencies)
