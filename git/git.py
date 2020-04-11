
import os

class Git:

    def __init__(self, gitUrl, branch, path):
        self.path = path
        self.branch = branch
        self.gitUrl = gitUrl

    def clone(self, module):
        projectPath = self.path + module
        os.popen('git clone ' + self.gitUrl + '/' + module +' temp/' + module).read()
        os.popen('git -C '+ projectPath +' checkout ' + self.branch).read()
        os.popen('git -C '+ projectPath +' pull ').read()