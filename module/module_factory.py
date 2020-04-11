
from .module import Module
from .modules import Modules

class ModuleFactory:

    maven = None
    git = None

    def __init__(self, git,  maven):
        self.maven = maven
        self.git = git

    def createModules(self, rawModules):
        modules = Modules()
        for module in rawModules:
            modules.add(self.create(module))
        return modules

    def create(self, rawModule):
        self.git.clone(rawModule)
        version = self.maven.findModuleVersion(rawModule)
        return Module(rawModule, version)