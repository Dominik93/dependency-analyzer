import argparse
import configparser

parser = argparse.ArgumentParser(description='Live server for analyze dependencies')
parser.add_argument("--config-file", help='Configuration file, default config.ini', default='config.ini')
parser.add_argument("--host", help='Host', default='')
parser.add_argument("--port", help='Port', default=8080)
parser.add_argument("--interval", help='Interval', default=30)

args = parser.parse_args()

config = configparser.ConfigParser()
config.read(args.config_file)

git_url: str = config['GIT']['url']
branch: str = config['GIT']['branch']
modules: list[str] = list(map(str.strip, config['MODULES']['modules'].split(',')))
dependencies: list[str] = list(map(str.strip, config['DEPENDENCY']['dependencies'].split(',')))
packages: list[str] = list(map(str.strip, config['USAGE']['packages'].split(',')))
class_regexp: str = config['USAGE']['class_regexp']
print_strategy: str = 'html'
host: str = args.host
interval_in_minutes: int = int(args.interval)
port: int = int(args.port)
directory = config['DIRECTORY']['directory']
print(f"Service configuration {host}:{port} interval: {interval_in_minutes}")
print(f"Git configuration {git_url} branch: {branch}")
print(f"Analyzing configuration modules: {modules}, dependencies: {dependencies}, packages: {packages},"
      f" class_regexp: {class_regexp}, print_strategy: {print_strategy}")
