import pickle

class Dependencies:

    def __init__(self):
        self.dependencies = []
        self.mappedDependencies = {}
    
    def add(self, dependency):
        self.dependencies.append(dependency)
        self.mappedDependencies[dependency.getName()] = dependency

    def getDependency(self, name):
        return self.mappedDependencies[name]

    def get(self):
        return self.dependencies

    def load(self):
        with open('store.dependencies', 'rb') as configFile:
            self.dependencies = pickle.load(configFile)
            for dep in self.dependencies:
                self.mappedDependencies[dep.getName()] = dep
            
    def store(self):        
        with open('store.dependencies', 'wb') as configFile:
            pickle.dump(self.dependencies, configFile)