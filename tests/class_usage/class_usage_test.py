import unittest

from class_usage.class_usage_analyzer import ClassUsageAnalyzer
from class_usage.class_usage_matrix import ClassUsageMatrix
from maven.maven import Maven
from tests.mock_executor import MockExecutor


class MyTestCase(unittest.TestCase):
    def test_analyze_class_usage(self):
        maven = Maven(MockExecutor("/path", {}), [])
        modules = ['resources/first']
        packages = ["com.package.artifact"]
        class_regexp = ""
        analyzer = ClassUsageAnalyzer(maven, modules, packages, class_regexp)
        actual = analyzer.calculate_class_usage()
        matrix = ClassUsageMatrix(modules, packages)
        matrix.set_module_version('resources/first', "0.0.1")
        matrix.add_dependency_class_in_module("resources/first", "com.package.artifact",
                                              "com.package.artifact.Class1")
        matrix.add_dependency_class_in_module("resources/first", "com.package.artifact",
                                              "com.package.artifact.api.Class2")
        matrix.add_dependency_class_in_module("resources/first", "com.package.artifact",
                                              "com.package.artifact.package.Class3")
        self.assertEqual(matrix, actual)

    def test_analyze_class_usage_with_regexp(self):
        maven = Maven(MockExecutor("/path", {}), [])
        modules = ['resources/first']
        packages = ["com.package.artifact"]
        class_regexp = ".*api.*"
        analyzer = ClassUsageAnalyzer(maven, modules, packages, class_regexp)
        actual = analyzer.calculate_class_usage()
        matrix = ClassUsageMatrix(modules, packages)
        matrix.set_module_version('resources/first', "0.0.1")
        matrix.add_dependency_class_in_module("resources/first", "com.package.artifact",
                                              "com.package.artifact.api.Class2")
        self.assertEqual(matrix, actual)

    def test_analyze_class_usage_with_no_hits(self):
        maven = Maven(MockExecutor("/path", {}), [])
        modules = ['resources/first']
        packages = ["com.package.artifact2"]
        class_regexp = ""
        analyzer = ClassUsageAnalyzer(maven, modules, packages, class_regexp)
        actual = analyzer.calculate_class_usage()
        matrix = ClassUsageMatrix(modules, packages)
        matrix.set_module_version('resources/first', "0.0.1")
        self.assertEqual(matrix, actual)


if __name__ == '__main__':
    unittest.main()
