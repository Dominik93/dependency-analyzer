
class Module:

    name = ''

    version = 'unknown'

    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name + ':' + self.version
