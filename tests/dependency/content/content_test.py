import unittest
from dependency.dependency_matrix import DependencyMatrix
from dependency.content.html_dependency_content_provider import HtmlDependencyContentProvider
from dependency.content.plain_dependency_content_provider import PlainDependencyContentProvider


class ContentTestCase(unittest.TestCase):
    def test_console_content_provider(self):
        modules = ['sample', 'other']
        dependencies = ['com.sample:dependency', 'com.sample.other:dependency']
        matrix = DependencyMatrix(modules, dependencies)
        matrix.set_module_version("sample", "0.0.1")
        matrix.set_module_version("other", "0.0.2")
        matrix.set_dependency_version_in_module("sample", 'com.sample:dependency', "1.0.0")
        matrix.set_dependency_version_in_module("sample", 'com.sample.other:dependency', "2.0.0")
        matrix.set_dependency_version_in_module("other", 'com.sample:dependency', "2.0.0")
        matrix.set_dependency_version_in_module("other", 'com.sample.other:dependency', "2.0.0")

        printer = PlainDependencyContentProvider(matrix)
        actual = printer.get_content()
        self.assertEqual('''Dependency matrix:
              |  dependency  |  dependency  |  
-----------------------------------------------
sample 0.0.1  |  1.0.0       |  2.0.0       |  
other 0.0.2   |  2.0.0       |  2.0.0       |  
-----------------------------------------------''', actual)

    def test_html_content_provider(self):
        modules = ['first', 'second']
        dependencies = ['com.sample.first:dependency', 'com.sample.second:dependency']
        matrix = DependencyMatrix(modules, dependencies)
        matrix.set_module_version("first", "0.0.1")
        matrix.set_module_version("second", "0.0.2")
        matrix.set_dependency_version_in_module("first", 'com.sample.first:dependency', "1.0.0")
        matrix.set_dependency_version_in_module("first", 'com.sample.second:dependency', "2.0.0")
        matrix.set_dependency_version_in_module("second", 'com.sample.first:dependency', "2.0.0")
        matrix.set_dependency_version_in_module("second", 'com.sample.second:dependency', "2.0.0")

        printer = HtmlDependencyContentProvider(matrix)
        actual = printer.get_content()
        self.assertEqual('''<table id="modulesTable">
<tbody>
<tr class="header">
<th></th>
<th>dependency</th>
<th>dependency</th>
</tr>
<tr>
<td>first 0.0.1</td>
<td>1.0.0</td>
<td>2.0.0</td>
</tr>
<tr>
<td>second 0.0.2</td>
<td>2.0.0</td>
<td>2.0.0</td>
</tr>
</tbody>
</table>
''', actual)


if __name__ == '__main__':
    unittest.main()
