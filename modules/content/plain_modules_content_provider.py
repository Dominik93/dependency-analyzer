from class_usage.content.plain_class_usage_content_provider import PlainClassUsageContentProvider
from dependency.content.plain_dependency_content_provider import PlainDependencyContentProvider


class PlainModulesContentProvider:
    content = ""

    def __init__(self, modules, dependency_matrix, class_usage_matrix):
        self.modules = modules
        self.class_usage_matrix = class_usage_matrix
        self.dependency_matrix = dependency_matrix

    def get_content(self):
        content = ""
        content += PlainClassUsageContentProvider(self.class_usage_matrix).get_content()
        content += PlainDependencyContentProvider(self.dependency_matrix).get_content()
        return content
