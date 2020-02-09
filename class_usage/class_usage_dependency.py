
class ClassUsageDependency:

    name = ''

    classes = set()

    def __init__(self, name):
        self.name = name
        self.classes = set()

    def _addClass(self, aClass):
        self.classes.add(aClass)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
       return self.name + ':' + str(self.classes)
