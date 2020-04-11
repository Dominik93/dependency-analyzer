import pickle

from .html_class_usage_printer import HtmlClassUsagePrinter
from .html_dependency_printer import HtmlDependencyPrinter

class PrinterScheduler:

    def __init__(self, intervalInMunites, modules, dependencies):
        self. modules = modules
        self.dependencies = dependencies
        self.intervalInMunites = intervalInMunites

    def add(self, schedule):
        schedule.every(self.intervalInMunites).minutes.do(lambda : self.run())

    def run(self):
        print('Run printer scheduler')
        self.modules.load()
        self.dependencies.load()
        with open('store.class_usage_matrix', 'rb') as configFile:
            classUsageMatrix = pickle.load(configFile)
            HtmlClassUsagePrinter(classUsageMatrix, self.modules, self.dependencies).printClassUsageMatrix()
        with open('store.dependency_matrix', 'rb') as configFile:
            dependencyMatrix = pickle.load(configFile)
            HtmlDependencyPrinter(dependencyMatrix, self.modules, self.dependencies).printDependencyMatrix()
            
    
