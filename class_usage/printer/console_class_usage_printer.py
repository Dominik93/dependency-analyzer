
class ConsoleClassUsagePrinter:
    
    classUsageMatrix = {}

    def __init__ (self, classUsageMatrix):
        self.classUsageMatrix = classUsageMatrix


    def printClassUsageMatrix(self):
        print('Class usage matrix:')
        print(self.classUsageMatrix)
