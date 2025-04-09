class Dependency:
    name = ''

    version = 'unknown'

    def __init__(self, name):
        self.name = name
        self.version = 'unknown'

    def _setVersion(self, version):
        self.version = version

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name + ':' + self.version
