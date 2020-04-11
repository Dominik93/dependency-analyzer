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

gitUrl = config['GIT']['url']
branch = config['GIT']['branch']

rawModules = list(map(str.strip, config['MODULES']['modules'].split(',')))
rawDependencies = list(map(str.strip, config['DEPENDENCY']['dependencies'].split(',')))
rawPackages = list(map(str.strip, config['CLASS_USAGE']['packages'].split(',')))

classRegexp = config['CLASS_USAGE']['class_regexp']

host = args.host
intervalInMunites = int(args.interval)
port = int(args.port)
