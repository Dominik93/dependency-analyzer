class ConsoleClassUsagePrinter:
    class_usage_matrix = {}

    def __init__(self, class_usage_matrix):
        self.class_usage_matrix = class_usage_matrix

    def print_class_usage_matrix(self):
        print('Class usage matrix:')
        print(self.class_usage_matrix)
