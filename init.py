import sys
import os
import configparser
import shutil
import argparse

from list_util import stripArray

parser = argparse.ArgumentParser(description='Tool for analyze dependencies')
parser.add_argument("--config-file", help='Configuration file, default config.ini', default='config.ini')
parser.add_argument("--search-dependency", help='Search for dependency in modules', action='store_true')
parser.add_argument("--search-usage", help='Scan project searching for class usage', action='store_true')
parser.add_argument("--no-clean-up", help='Remove all projects', action='store_false')
args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config_file)
gitUrl = config['GIT']['url']
cleanUp = args.no_clean_up
searchDependency = args.search_dependency
searchUsage = args.search_usage
branch = config['GIT']['branch']
modules = stripArray(config['PROJECTS']['modules'].split(','))
dependencies = stripArray(config['PROJECTS']['dependencies'].split(','))
packages = stripArray(config['PROJECTS']['packages'].split(','))
