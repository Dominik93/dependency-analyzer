
from class_usage.class_usage_analyzer import ClassUsageAnalyzer

class ClassUsageScheduler:

    def __init__(self, intervalInMunites, modules, packages, classRegexp):
        self.modules = modules
        self.packages = packages
        self.classRegexp = classRegexp
        self.intervalInMunites = intervalInMunites

    def add(self, schedule):
        schedule.every(self.intervalInMunites).minutes.do(lambda : self.run())

    def run(self):
        print('Run class usage scheduler')
        self.modules.load()
        analyzer = ClassUsageAnalyzer(self.modules, self.packages, self.classRegexp)
        analyzer.calcualteClassUsage()
        analyzer.store()
