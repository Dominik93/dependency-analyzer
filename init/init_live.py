import configparser
import argparse

parser = argparse.ArgumentParser(description='Live server for analyze dependencies')
parser.add_argument("--config-file", help='Configuration file, default config.ini', default='config.ini')
parser.add_argument("--host", help='Host', default='')
parser.add_argument("--port", help='Port', default=8080)
parser.add_argument("--interval", help='Interval', default=30)

args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config_file)

git_url = config['GIT']['url']
branch = config['GIT']['branch']
modules = list(map(str.strip, config['MODULES']['modules'].split(',')))
dependencies = list(map(str.strip, config['DEPENDENCY']['dependencies'].split(',')))
packages = list(map(str.strip, config['USAGE']['packages'].split(',')))
class_regexp = config['USAGE']['class_regexp']
print_strategy = 'html'
host = args.host
interval_in_munites = int(args.interval)
port = int(args.port)
