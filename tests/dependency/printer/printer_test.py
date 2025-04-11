import unittest
from dependency.dependency_matrix import DependencyMatrix
from dependency.printer.html_dependency_factory import HtmlDependencyFactory
from dependency.printer.plain_dependency_factory import PlainDependencyFactory


class MyTestCase(unittest.TestCase):
    def test_console_printer(self):
        modules = ['resources/sample', 'resources/other']
        dependencies = ['com.sample:dependency', 'com.sample.other:dependency']
        matrix = DependencyMatrix(modules, dependencies)
        matrix.set_module_version("resources/sample", "0.0.1")
        matrix.set_module_version("resources/other", "0.0.2")
        matrix.set_dependency_version_in_module("resources/sample", 'com.sample:dependency', "1.0.0")
        matrix.set_dependency_version_in_module("resources/sample", 'com.sample.other:dependency', "2.0.0")
        matrix.set_dependency_version_in_module("resources/other", 'com.sample:dependency', "2.0.0")
        matrix.set_dependency_version_in_module("resources/other", 'com.sample.other:dependency', "2.0.0")

        printer = PlainDependencyFactory(matrix)
        actual = printer.print_dependency_matrix()
        self.assertEqual('''Dependency matrix:
                        |  dependency  |  dependency  |  
---------------------------------------------------------
resources/sample 0.0.1  |  1.0.0       |  2.0.0       |  
resources/other 0.0.2   |  2.0.0       |  2.0.0       |  
---------------------------------------------------------''', actual)

    def test_html_printer(self):
        modules = ['resources/first', 'resources/second']
        dependencies = ['com.sample.first:dependency', 'com.sample.second:dependency']
        matrix = DependencyMatrix(modules, dependencies)
        matrix.set_module_version("resources/first", "0.0.1")
        matrix.set_module_version("resources/second", "0.0.2")
        matrix.set_dependency_version_in_module("resources/first", 'com.sample.first:dependency', "1.0.0")
        matrix.set_dependency_version_in_module("resources/first", 'com.sample.second:dependency', "2.0.0")
        matrix.set_dependency_version_in_module("resources/second", 'com.sample.first:dependency', "2.0.0")
        matrix.set_dependency_version_in_module("resources/second", 'com.sample.second:dependency', "2.0.0")

        printer = HtmlDependencyFactory(matrix)
        actual = printer.print_dependency_matrix()
        self.assertEqual('''<table id="modulesTable">
<tbody>
<tr class="header">
<th></th>
<th>dependency</th>
<th>dependency</th>
</tr>
<tr>
<td>resources/first 0.0.1</td>
<td>1.0.0</td>
<td>2.0.0</td>
</tr>
<tr>
<td>resources/second 0.0.2</td>
<td>2.0.0</td>
<td>2.0.0</td>
</tr>
</tbody>
</table>
''', actual)


if __name__ == '__main__':
    unittest.main()
