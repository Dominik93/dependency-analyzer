import sys
import os
import configparser
import shutil
import argparse

from list_util import stripArray

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
    modules = stripArray(config['MODULES']['modules'].split(','))
else :
    modules = stripArray(args.only_include_modules.split(','))
    
if len(args.only_include_dependencies) == 0:
    dependencies = stripArray(config['DEPENDENCY']['dependencies'].split(','))
else :
    dependencies = stripArray(args.only_include_dependencies.split(','))
    
packages = stripArray(config['USAGE']['packages'].split(','))

classRegexp = config['USAGE']['class_regexp']

printStrategy = args.print