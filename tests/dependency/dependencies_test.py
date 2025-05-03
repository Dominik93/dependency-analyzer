import unittest
from dependency.dependency_analyzer import DependenciesAnalyzer
from dependency.dependency_matrix import DependencyMatrix
from maven.maven import Maven
from tests.mock_executor import MockExecutor


directory = "./resources"

class DependenciesTestCase(unittest.TestCase):
    def test_dependencies_analyzer_single_module_single_dependency(self):
        mock = {"mvn -f ./resources/first dependency:tree -Dincludes=com.sample.first:dependency":
                    '''
                    [INFO] Scanning for projects...
                    [INFO] 
                    [INFO] ----------------------< com.sample.first:sample >-----------------------
                    [INFO] Building sample 0.0.1
                    [INFO]   from pom.xml
                    [INFO] --------------------------------[ jar ]---------------------------------
                    [INFO]
                    [INFO] --- dependency:3.6.1:tree (default-cli) @ sample ---
                    [INFO] com.sample.first:sample:jar:0.0.1
                    [INFO] \- com.sample.first:dependency:jar:1.0.0:compile
                    [INFO] ------------------------------------------------------------------------
                    [INFO] BUILD SUCCESS
                    [INFO] ------------------------------------------------------------------------
                    [INFO] Total time:  1.634 s
                    [INFO] Finished at: 2025-04-10T19:53:52+02:00
                    [INFO] ------------------------------------------------------------------------
                    '''}
        modules = ['first']
        dependencies = ['com.sample.first:dependency']
        maven = Maven(directory, MockExecutor(mock), dependencies)
        analyzer = DependenciesAnalyzer(maven, modules, dependencies)
        actual = analyzer.calculate_dependencies(directory)

        expected = DependencyMatrix(modules, dependencies)
        expected.set_module_version("first", "0.0.1")
        expected.set_dependency_version_in_module("first", 'com.sample.first:dependency', "1.0.0")
        self.assertEqual(actual, expected)

    def test_dependencies_analyzer_single_module_multiple_dependency(self):
        mock = {
            "mvn -f ./resources/first dependency:tree -Dincludes=com.sample.first:dependency,com.sample.second:dependency":
                '''
                    [INFO] Scanning for projects...
                    [INFO] 
                    [INFO] ----------------------< com.sample.first:sample >-----------------------
                    [INFO] Building sample 0.0.1
                    [INFO]   from pom.xml
                    [INFO] --------------------------------[ jar ]---------------------------------
                    [INFO]
                    [INFO] --- dependency:3.6.1:tree (default-cli) @ sample ---
                    [INFO] com.sample.first:sample:jar:0.0.1
                    [INFO] +- com.sample.first:dependency:jar:1.0.0:compile
                    [INFO] \- com.sample.second:dependency:jar:2.0.0:compile
                    [INFO] ------------------------------------------------------------------------
                    [INFO] BUILD SUCCESS
                    [INFO] ------------------------------------------------------------------------
                    [INFO] Total time:  2.369 s
                    [INFO] Finished at: 2025-04-10T19:56:02+02:00
                    [INFO] ------------------------------------------------------------------------
                    '''}
        modules = ['first']
        dependencies = ['com.sample.first:dependency', 'com.sample.second:dependency']
        maven = Maven(directory, MockExecutor(mock), dependencies)
        analyzer = DependenciesAnalyzer(maven, modules, dependencies)
        actual = analyzer.calculate_dependencies(directory)

        expected = DependencyMatrix(modules, dependencies)
        expected.set_module_version("first", "0.0.1")
        expected.set_dependency_version_in_module("first", 'com.sample.first:dependency', "1.0.0")
        expected.set_dependency_version_in_module("first", 'com.sample.second:dependency', "2.0.0")
        self.assertEqual(actual, expected)

    def test_dependencies_analyzer_multiple_module_multiple_dependency(self):
        mock = {
            "mvn -f ./resources/first dependency:tree -Dincludes=com.sample.first:dependency,com.sample.second:dependency":
                '''
                    [INFO] Scanning for projects...
                    [INFO] 
                    [INFO] -------------------------< com.sample:sample >--------------------------
                    [INFO] Building sample 0.0.1
                    [INFO]   from pom.xml
                    [INFO] --------------------------------[ jar ]---------------------------------
                    [INFO] 
                    [INFO] --- dependency:3.6.1:tree (default-cli) @ sample ---
                    [INFO] com.sample:sample:jar:0.0.1
                    [INFO] +- com.sample.first:dependency:jar:1.0.0:compile
                    [INFO] \- com.sample.second:dependency:jar:2.0.0:compile
                    [INFO] ------------------------------------------------------------------------
                    [INFO] BUILD SUCCESS
                    [INFO] ------------------------------------------------------------------------
                    [INFO] Total time:  1.551 s
                    [INFO] Finished at: 2025-04-09T19:31:37+02:00
                    [INFO] ------------------------------------------------------------------------
                    ''',
            "mvn -f ./resources/second dependency:tree -Dincludes=com.sample.first:dependency,com.sample.second:dependency":
                '''
                    [INFO] Scanning for projects...
                    [INFO] 
                    [INFO] -------------------------< com.sample:sample >--------------------------
                    [INFO] Building sample 0.0.1
                    [INFO]   from pom.xml
                    [INFO] --------------------------------[ jar ]---------------------------------
                    [INFO] 
                    [INFO] --- dependency:3.6.1:tree (default-cli) @ sample ---
                    [INFO] com.sample:sample:jar:0.0.1
                    [INFO] +- com.sample.first:dependency:jar:2.0.0:compile
                    [INFO] \- com.sample.second:dependency:jar:2.0.0:compile
                    [INFO] ------------------------------------------------------------------------
                    [INFO] BUILD SUCCESS
                    [INFO] ------------------------------------------------------------------------
                    [INFO] Total time:  1.551 s
                    [INFO] Finished at: 2025-04-09T19:31:37+02:00
                    [INFO] ------------------------------------------------------------------------
                    '''}
        modules = ['first', 'second']
        dependencies = ['com.sample.first:dependency', 'com.sample.second:dependency']
        maven = Maven(directory, MockExecutor(mock), dependencies)
        analyzer = DependenciesAnalyzer(maven, modules, dependencies)
        actual = analyzer.calculate_dependencies(directory)

        expected = DependencyMatrix(modules, dependencies)
        expected.set_module_version("first", "0.0.1")
        expected.set_module_version("second", "0.0.2")
        expected.set_dependency_version_in_module("first", 'com.sample.first:dependency', "1.0.0")
        expected.set_dependency_version_in_module("first", 'com.sample.second:dependency', "2.0.0")
        expected.set_dependency_version_in_module("second", 'com.sample.first:dependency', "2.0.0")
        expected.set_dependency_version_in_module("second", 'com.sample.second:dependency', "2.0.0")
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
