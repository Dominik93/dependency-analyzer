from init import *
from os import walk
from list_util import maxLength
from matrix_printer import printDependencyMatrix


def retrivePackage(string): 
    return string.split(':')[0]

def dependenciesToIncludesOption(dependencies):
    str = ''
    for dependency in dependencies:
        str = str + dependency+ ' '
    return '-Dincludes=' + str.strip().replace(' ', ',')

def initDependenciesMatrix():
    matrix = {}        
    for module in modules:
        matrix[module] = {}
        for dependency in dependencies:
            matrix[module][dependency] = ''

    return matrix


def initUsageMatrix():
    matrix = {}        
    for module in modules:
        matrix[module] = {}
        for package in packages:
            matrix[module][package] = set([])
    return matrix

def cloneAllProjects():
    print('Clone modules: ' + str(modules))
    for module in modules:
        projectPath = os.getcwd() + '/' + module
        os.popen('git clone ' + gitUrl + '/' + module).read()
        os.popen('git -C '+ projectPath +' checkout ' + branch).read()
        os.popen('git -C '+ projectPath +' pull ').read()

def removeProjects():
    print('Clean up')
    for module in modules:
        projectPath = os.getcwd() + '/' + module
        os.popen('rd /s /q "' + projectPath + '"')

def calculateDependencies(dependenyMatrix):
    print('Dependencies: ' + str(dependencies))
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
    return dependenyMatrix

def strip(string):
    return string.replace('import  ', '').replace('\n', '')

def calcualteUsage(usageMatrix):
    for module in modules:
        projectPath = os.getcwd() + '/' + module
        print('Analize ' + module)
        for (dirpath, dirnames, filenames) in walk(projectPath):
            for file in filenames:
                if '.java' in  file:
                    path = dirpath + '\\' + file
                    #print('Open ' + path)
                    f = open(path, "r")
                    lines = f.readlines()
                    f.close()
                    for line in lines:
                        for package in packages:
                            if package in line and 'import' in line: 
                                print('Found ' + line + ' in ' + path)
                                usageMatrix[module][package].add(strip(line))
    return usageMatrix

dependencyMatrix = initDependenciesMatrix()
usageMatrix = initUsageMatrix()
includesOption = dependenciesToIncludesOption(dependencies)
try:
    cloneAllProjects()
    #dependencyMatrix = calculateDependencies(dependencyMatrix)
    #printDependencyMatrix(dependencyMatrix)

    if searchUsage:
        usageMatrix = calcualteUsage(usageMatrix)
        print(usageMatrix)

finally:    
    if cleanUp:
        removeProjects()
