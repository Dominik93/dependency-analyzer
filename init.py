import sys
import os
import configparser
import shutil
import argparse

from list_util import stripArray

parser = argparse.ArgumentParser(description='Tool for analyze dependencies')
parser.add_argument("--config-file", help='Configuration file, default config.ini', default='config.ini')
args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config_file)
gitUrl = config['GIT']['url']
branch = config['GIT']['branch']
modules = stripArray(config['PROJECTS']['modules'].split(','))
dependencies = stripArray(config['PROJECTS']['dependencies'].split(','))
