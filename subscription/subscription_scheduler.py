
class SubscriptionScheduler:

    oldDependencies = {}

    def __init__(self, intervalInMunites, dependencies):
        self.dependencies = dependencies
        self.dependencies.load()
        self.oldDependencies = self.dependencies
        self.intervalInMunites = intervalInMunites

    def add(self, schedule):
        schedule.every(self.intervalInMunites).minutes.do(lambda : self.run())

    def run(self):
        print('Run subscription scheduler')
        self.dependencies.load()
        for oldDep in self.oldDependencies.get(): 
            newDep = self.dependencies.getDependency(oldDep.getName())
            if (oldDep.version != newDep.version):
                print("New Dependency!")



