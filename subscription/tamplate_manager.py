from string import Template

def readTemplate(fileName):
    with open(fileName, 'r', encoding='utf-8') as templateFile:
        templateFileContent = templateFile.read()
    return Template(templateFileContent)