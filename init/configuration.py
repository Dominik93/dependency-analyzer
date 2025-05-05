class Configuration:

    def __init__(self, git_configuration, analyze_configuration, server_configuration, project_configuration,
                 print_strategy, interval_in_minutes):
        self.git_configuration: GitConfiguration = git_configuration
        self.server_configuration: ServerConfiguration = server_configuration
        self.analyze_configuration: AnalyzeConfiguration = analyze_configuration
        self.print_strategy: str = print_strategy
        self.interval_in_minutes: int = interval_in_minutes
        self.project_configuration: ProjectConfiguration = project_configuration

    def __str__(self):
        return str(self.__dict__)


class AnalyzeConfiguration:

    def __init__(self, modules, search_dependency, dependencies, search_class_usage, packages, class_regexp):
        self.modules: list[str] = modules
        self.dependencies: list[str] = dependencies
        self.search_class_usage = search_class_usage
        self.search_dependency = search_dependency
        self.packages: list[str] = packages
        self.class_regexp: str = class_regexp

    def __str__(self):
        return str(self.__dict__)


class ServerConfiguration:

    def __init__(self, host, port):
        self.host: str = host
        self.port: int = port

    def __str__(self):
        return str(self.__dict__)


class ProjectConfiguration:
    def __init__(self, clean_up, directory):
        self.clean_up: str = clean_up
        self.directory: str = directory

    def __str__(self):
        return str(self.__dict__)


class GitConfiguration:

    def __init__(self, git_url, branch):
        self.git_url: str = git_url
        self.branch: str = branch

    def __str__(self):
        return str(self.__dict__)
