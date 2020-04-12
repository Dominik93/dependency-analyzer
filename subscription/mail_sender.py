
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class MailSender:

    def __init__(self, mailConfig):
        self.mailConfig = mailConfig

    def sentMail(self, subject, template, properties):
        smtpSession = smtplib.SMTP(host=self.mailConfig['host'], port=self.mailConfig['port'])
        smtpSession.starttls()
        smtpSession.login(self.mailConfig['sender'], self.mailConfig['password'])
        msg = MIMEMultipart()
        
        message = template.substitute(NAME=properties['NAME'], NEW_VERSION=properties['NEW_VERSION'])
        print(message)

        msg['From']=self.mailConfig['sender']
        msg['To']=self.mailConfig['recipient']
        msg['Subject']=subject
        msg.attach(MIMEText(message, 'plain'))
        smtpSession.send_message(msg)
        del msg
        smtpSession.quit()    
