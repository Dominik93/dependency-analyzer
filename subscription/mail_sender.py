
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .mail_config import MailConfig

class MailSender:

    def __init__(self, mailConfig, config, modules):
        self.mailConfig = mailConfig
        self.subscriptions = {}
        for module in modules.get():
            subscriptionsForModule = []
            for mail in config['SUBSCRIPTION']['default_recipient'].split(','):
                subscriptionsForModule.append(mail)
            for mail in config['SUBSCRIPTION'][module].split(','):
                subscriptionsForModule.append(mail)
            self.subscriptions[module] = subscriptionsForModule

    def sentMail(self, mailConfig: MailConfig, template, recipients = []):
        s = smtplib.SMTP(host=mailConfig.host, port=mailConfig.port)
        s.starttls()
        s.login(mailConfig.address, mailConfig.password)
        for recipient in recipients:
            msg = MIMEMultipart()
            
            message = template

            print(message)

            msg['From']=mailConfig.address
            msg['To']=recipient
            msg['Subject']="Dependency notification"
            
            msg.attach(MIMEText(message, 'plain'))
        
            s.send_message(msg)
            del msg
        s.quit()    
