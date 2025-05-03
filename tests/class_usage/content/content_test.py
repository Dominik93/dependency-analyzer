import unittest

from class_usage.class_usage_matrix import ClassUsageMatrix
from class_usage.content.html_class_usage_content_provider import HtmlClassUsageContentProvider
from class_usage.content.plain_class_usage_content_provider import PlainClassUsageContentProvider


class ContentProviderTestCase(unittest.TestCase):
    def test_plain_content_provider(self):
        modules = ['first']
        packages = ["com.package.artifact"]
        matrix = ClassUsageMatrix(modules, packages)
        matrix.add_dependency_class_in_module("first", "com.package.artifact",
                                              "com.package.artifact.api.Class2")

        printer = PlainClassUsageContentProvider(matrix)
        actual = printer.get_content()
        self.assertEqual(
            "Class usage matrix:{'first': first:unknown Class usages: {'com.package.artifact': com.package.artifact:{'com.package.artifact.api.Class2'}}}",
            actual)

    def test_html_content_provider(self):
        modules = ['first']
        packages = ["com.package.artifact"]
        matrix = ClassUsageMatrix(modules, packages)
        matrix.set_module_version("first", "0.0.1")
        matrix.add_dependency_class_in_module("first", "com.package.artifact",
                                              "com.package.artifact.api.Class2")

        printer = HtmlClassUsageContentProvider(matrix, "classUsagesTable")
        actual = printer.get_content()
        self.assertEqual('''<table id="classUsagesTable">
<tbody>
<tr class="header">
<th></th>
<th>com.package.artifact</th>
</tr>
<tr>
<td>first 0.0.1</td>
<td>com.package.artifact.api.Class2
</td>
</tr>
</tbody>
</table>
''', actual)


if __name__ == '__main__':
    unittest.main()
