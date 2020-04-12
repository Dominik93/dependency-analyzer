
from .dependency_factory import DependencyFactory


class DependenciesScheduler:

    def __init__(self, git, maven, intervalInMunites):
        self.maven = maven
        self.intervalInMunites = intervalInMunites
        self.git = git
        self.dependencyFactory = DependencyFactory(self.git, self.maven)

    def add(self, schedule, rawDependencies):
        schedule.every(self.intervalInMunites).minutes.do(lambda : self.run(rawDependencies))
        self.run(rawDependencies)

    def run(self, rawDependencies):
        print('Run dependencies scheduler')
        dependencies = self.dependencyFactory.createDependencies(rawDependencies)
        dependencies.store()

