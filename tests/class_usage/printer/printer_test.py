import unittest

from class_usage.class_usage_matrix import ClassUsageMatrix
from class_usage.printer.html_class_usage_factory import HtmlClassUsageFactory
from class_usage.printer.plain_class_usage_factory import PlainClassUsageFactory


class MyTestCase(unittest.TestCase):
    def test_plain_printer(self):
        modules = ['resources/first']
        packages = ["com.package.artifact"]
        matrix = ClassUsageMatrix(modules, packages)
        matrix.add_dependency_class_in_module("resources/first", "com.package.artifact",
                                              "com.package.artifact.api.Class2")

        printer = PlainClassUsageFactory(matrix)
        actual = printer.print_class_usage_matrix()
        self.assertEqual("Class usage matrix:{'resources/first': resources/first:unknown Class usages: {'com.package.artifact': com.package.artifact:{'com.package.artifact.api.Class2'}}}", actual)


    def test_html_printer(self):
        modules = ['resources/first']
        packages = ["com.package.artifact"]
        matrix = ClassUsageMatrix(modules, packages)
        matrix.set_module_version("resources/first", "0.0.1")
        matrix.add_dependency_class_in_module("resources/first", "com.package.artifact",
                                              "com.package.artifact.api.Class2")

        printer = HtmlClassUsageFactory(matrix)
        actual = printer.print_class_usage_matrix()
        self.assertEqual('''<table id="classUsagesTable">
<tbody>
<tr class="header">
<th></th>
<th>com.package.artifact</th>
</tr>
<tr>
<td>resources/first 0.0.1</td>
<td>com.package.artifact.api.Class2
</td>
</tr>
</tbody>
</table>
''', actual)



if __name__ == '__main__':
    unittest.main()
