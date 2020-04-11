import pickle

class DependenciesAnalyzer:

    def __init__(self, maven, modules, dependencies):
        print('Modules: ' + str(modules.get()))
        print('Dependencies: ' + str(dependencies.get()))
        self.maven = maven
        self.modules = modules
        self.dependencyMatrix = {}
        self.dependencies = dependencies

    def store(self):        
        with open('store.dependency_matrix', 'wb') as configFile:
            pickle.dump(self.dependencyMatrix, configFile)

    def calculateDependencies(self):
        for module in self.modules.get():
            print('Analyze ' + module.name)
            dependencyTree = self.maven.dependencyTree(module, self.dependencies)
            for dependency in self.dependencies.get():
                if dependency.getName() in dependencyTree:
                    indexOfDependency = dependencyTree.find(dependency.getName()+":")
                    dependencyFromTree = dependencyTree[indexOfDependency: dependencyTree.find('\n', indexOfDependency)]
                    dependencyVersion = dependencyFromTree.split(':')[3] 
                    if module.name not in self.dependencyMatrix:
                        self.dependencyMatrix[module.name] = {}
                    self.dependencyMatrix[module.name][dependency.artifactId] = dependencyVersion
                else:
                    self.dependencyMatrix[module.name][dependency.artifactId] = ''   
 