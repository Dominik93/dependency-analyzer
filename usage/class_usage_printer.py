from init import modules, dependencies, packages
from list_util import maxLength

def printUsageMatrix(usageMatrix):
    print('Usage matrix:')
    for module in usageMatrix.keys():
        print('Module: ' + module)	
        for dependency in usageMatrix[module].keys():
            if len(usageMatrix[module][dependency]) > 0:
                print('Dependency:' + dependency)
                for item in usageMatrix[module][dependency]:
                    print('\t' + str(item))
