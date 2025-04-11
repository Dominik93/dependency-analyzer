class Dependency:
    name: str = ''

    version: str = 'unknown'

    def __init__(self, name: str):
        self.name = name
        self.version = 'unknown'

    def set_version(self, version: str) -> None:
        self.version = version

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name + ':' + self.version

    def __eq__(self, other):
        if not isinstance(other, Dependency):
            return NotImplemented

        return self.name == other.name and self.version == other.version
