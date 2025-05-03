
class FilePrinter:

    def __init__(self, content: str, dir_path: str, file: str):
        self.content = content
        self.dir_path = dir_path
        self.file = file

    def print(self):
        file = self.dir_path + "/" + self.file
        print(f'Write to {file}')
        f = open(file, 'w')
        f.write(self.content)
        f.close()
