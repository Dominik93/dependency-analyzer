from class_usage.content.html_class_usage_content_provider import HtmlClassUsageContentProvider
from dependency.content.html_dependency_content_provider import HtmlDependencyContentProvider


class HtmlModulesContentProvider:

    def __init__(self, modules, dependency_matrix, class_usage_matrix):
        self.modules = modules
        self.class_usage_matrix = class_usage_matrix
        self.dependency_matrix = dependency_matrix

    def get_content(self):
        content = ""
        for module in self.modules:
            content += f'<button type="button" class="collapsible">{module}</button>'
            content += f'<div class="content">'
            content += HtmlDependencyContentProvider(self.dependency_matrix, lambda x: x == module).get_content()
            content += HtmlClassUsageContentProvider(self.class_usage_matrix, lambda x: x == module).get_content()
            content += f'</div>'
            content += f"</br></br>"
        return content
