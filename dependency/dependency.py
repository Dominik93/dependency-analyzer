

class Dependency:

    def __init__(self, groupId, artifactId, version, project=None):
        self.groupId = groupId
        self.project = project
        self.version = version
        self.artifactId = artifactId

    def getName(self):
        return self.groupId + ':' + self.artifactId

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.project == None or self.project == '':
            return self.groupId + ':' + self.artifactId
        return self.project + '|' + self.groupId + ':' + self.artifactId + ':' + self.version
