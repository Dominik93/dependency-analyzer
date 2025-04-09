import os
import re
from .class_usage_matrix import ClassUsageMatrix


class ClassUsageAnalyzer:
    modules = []
    packages = []

    class_regexp = ''

    matrix: ClassUsageMatrix = {}

    def __init__(self, modules, packages, class_regexp):
        self.matrix = ClassUsageMatrix(modules, packages)
        self.modules = modules
        self.packages = packages
        self.class_regexp = class_regexp

    def calculate_class_usage(self):
        for module in self.modules:
            project_path = os.getcwd() + '/temp/' + module
            print('Analize ' + module)
            for (dirpath, dirnames, filenames) in os.walk(project_path):
                for file in filenames:
                    if '.java' in file:
                        path = dirpath + '\\' + file
                        f = open(path, "r", encoding="utf8")
                        lines = f.readlines()
                        f.close()
                        for line in lines:
                            for package in self.packages:
                                if package in line and 'import' in line:
                                    class_with_package = self.__strip_import(line)
                                    if re.search(self.class_regexp, class_with_package):
                                        self.matrix.add_dependency_class_in_module(module, package, class_with_package)
        return self.matrix

    def __strip_import(self, string):
        return string.replace('import ', '').replace('\n', '').replace(';', '')
