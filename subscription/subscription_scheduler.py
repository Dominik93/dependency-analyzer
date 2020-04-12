
from .mail_sender import MailSender

from .tamplate_manager import readTemplate

class SubscriptionScheduler:

    oldDependencies = {}

    def __init__(self, intervalInMunites, dependencies, mailSender):
        self.dependencies = dependencies
        self.dependencies.load()
        self.oldDependencies = self.dependencies
        self.intervalInMunites = intervalInMunites
        self.mailSender = mailSender

    def add(self, schedule):
        schedule.every(self.intervalInMunites).minutes.do(lambda : self.run())

    def run(self):
        print('Run subscription scheduler')
        self.dependencies.load()
        for oldDep in self.oldDependencies.get(): 
            newDep = self.dependencies.getDependency(oldDep.getName())
            if (oldDep.version != newDep.version):
                template = readTemplate('subscription/dependency_template.txt')
                properties = {}
                properties['NAME'] = newDep.artifactId
                properties['NEW_VERSION'] = newDep.version
                self.mailSender.sentMail("Dependency notification", template, properties)



