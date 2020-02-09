import os
from init.init_manual import gitUrl, branch, modules, dependencies, printStrategy, packages, cleanUp, searchClassUsage, searchDependency, classRegexp
from analyze import analyzeClassUsage, analyzeDependencies, cloneAllProjects, removeProjects

try:
    cloneAllProjects(gitUrl, branch, modules)
    if searchDependency:
       analyzeDependencies(modules, dependencies, printStrategy)

    if searchClassUsage:
        analyzeClassUsage(modules, packages, classRegexp, printStrategy)

finally:    
    if cleanUp:
        removeProjects(modules)