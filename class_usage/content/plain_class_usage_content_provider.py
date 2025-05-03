class PlainClassUsageContentProvider:
    content = ""

    def __init__(self, class_usage_matrix):
        self.class_usage_matrix = class_usage_matrix

    def get_content(self):
        self.content += 'Class usage matrix:'
        self.content += str(self.class_usage_matrix)
        return self.content
