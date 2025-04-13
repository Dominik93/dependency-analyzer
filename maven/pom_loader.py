import os

import xmltodict


def find_module_version(module: str) -> str:
    project_path = os.getcwd() + '/temp/' + module + "/pom.xml"
    with open(project_path, "rb") as file:
        pom = xmltodict.parse(file)
        return pom['project']['version']
