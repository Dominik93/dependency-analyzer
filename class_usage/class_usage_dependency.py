class ClassUsageDependency:
    name = ''

    classes = set()

    def __init__(self, name):
        self.name = name
        self.classes = set()

    def _add_class(self, a_class):
        self.classes.add(a_class)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name + ':' + str(self.classes)

    def __eq__(self, other):
        if not isinstance(other, ClassUsageDependency):
            return NotImplemented

        return self.name == other.name and self.classes == other.classes
