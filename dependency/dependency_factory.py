
from .dependency import Dependency
from .dependencies import Dependencies

class DependencyFactory:

    def __init__(self, git, maven):
        self.maven = maven
        self.git = git

    def createDependencies(self, rawDependencies):
        dependencies = Dependencies()
        for dependncy in rawDependencies:
            dependencies.add(self.create(dependncy))
        return dependencies

    def create(self, rawDependency):
        if('|' in rawDependency):
            project = rawDependency.split("|")[0]
            groupId = rawDependency.split("|")[1].split(':')[0]
            artifactId = rawDependency.split("|")[1].split(':')[1]
            self.git.clone(project)
            version = self.maven.findModuleVersion(project)
            return Dependency(groupId, artifactId, version, project)
        else:
            groupId = rawDependency.split(':')[0]
            artifactId = rawDependency.split(':')[1]
            version = 'unknown'
            return Dependency(groupId, artifactId, version)