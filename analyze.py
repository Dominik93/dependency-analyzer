from init import *

def dependenciesToIncludesOption(dependencies):
    str = ''
    for dependency in dependencies:
        str = str + dependency+ ' '
    return '-Dincludes=' + str.strip().replace(' ', ',')

def initDependencyMatrix():
    matrix = {}        
    for module in modules:
        matrix[module] = {}
    return matrix

def cloneAllProjects():
    print('Clone modules: ' + str(modules))
    for module in modules:
        projectPath = os.getcwd() + '/' + module
        os.popen('git clone ' + gitUrl + '/' + module).read()
        os.popen('git -C '+ projectPath +' checkout ' + branch)

def cleanUp():
    print('Clean up')
    for module in modules:
        projectPath = os.getcwd() + '/' + module
        os.popen('rd /s /q "' + projectPath + '"')

def calculateDependencies():
    for module in modules:
        projectPath = os.getcwd() + '/' + module
        print('Analize ' + module)
        dependencyTree = os.popen('mvn -f ' + projectPath + ' dependency:tree ' + includesOption).read()
        for dependency in dependencies:
            if dependency in dependencyTree:
                indexOfDependency = dependencyTree.find(dependency)
                dependencyFromTree = dependencyTree[indexOfDependency: dependencyTree.find('\n', indexOfDependency)]
                dependencyVersion = dependencyFromTree.split(':')[3] 
                dependencyMatrix[module][dependency] = dependencyVersion
                print('Found ' + dependency +'\tversion: ' + dependencyVersion)
            else:
                dependencyMatrix[module][dependency] = ''        

def fillWith(string, width = 25, fill = '.'):
    return string.ljust(width, fill)

def printDependencyMatrix():
    print('Dependency matrix:')
    dependenciesHeaders = fillWith('', 25, ' ') + '\t'
    for dependency in dependencies:
        dependenciesHeaders += fillWith(dependency.split(':')[1], 20, ' ') + '\t' 
    print(dependenciesHeaders)
    for module in modules:
        moduleRow = fillWith(module, 25, '.') + '\t'
        for dependency in dependencies:
            moduleRow += fillWith(dependencyMatrix[module][dependency], 20, ' ') + '\t'
        print(moduleRow)

dependencyMatrix = initDependencyMatrix()
includesOption = dependenciesToIncludesOption(dependencies)
try:
    cloneAllProjects()
    calculateDependencies()
    printDependencyMatrix()
finally:    
    cleanUp()
