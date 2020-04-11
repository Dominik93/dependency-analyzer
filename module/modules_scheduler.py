
from .module_factory import ModuleFactory

class ModulesScheduler:

    def __init__(self, git, maven, intervalInMunites):
        self.maven = maven
        self.intervalInMunites = intervalInMunites
        self.git = git
        self.moduleFactory = ModuleFactory(self.git, self.maven)

    def add(self, schedule, rawModules):
        schedule.every(self.intervalInMunites).minutes.do(lambda : self.run(rawModules))

    def run(self, rawModules):
        print('Run modules scheduler')
        modules = self.moduleFactory.createModules(rawModules)
        modules.store()
