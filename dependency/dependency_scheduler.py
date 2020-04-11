
from .dependency_analyzer import DependenciesAnalyzer
from .dependency_factory import DependencyFactory

class DependencyScheduler:

    def __init__(self, maven, intervalInMunites, dependencyFactory, moduleFactory):
        self.maven = maven
        self.dependencyFactory = dependencyFactory
        self.moduleFactory = moduleFactory
        self.intervalInMunites = intervalInMunites

    def add(self, schedule, rawModules, rawDependencies):
        schedule.every(self.intervalInMunites).minutes.do(lambda : self.run(rawModules, rawDependencies))

    def run(self, rawModules, rawDependencies):
        print('Run dependency matrix scheduler')
        dependencies = self.dependencyFactory.createDependencies(rawDependencies)
        modules = self.moduleFactory.createModules(rawModules)
        self.analyzer = DependenciesAnalyzer(self.maven, modules, dependencies)
        self.analyzer.calculateDependencies()
        self.analyzer.store()
