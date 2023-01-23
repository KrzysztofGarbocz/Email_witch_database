"""Sending mail module"""
import ssl
import smtplib
from email.message import EmailMessage
from string import Template
from os import getenv
from dotenv import load_dotenv
load_dotenv()


class Sender:
    """Class to sending mail"""
    def __init__(self):
        self.smtp_server = getenv('SMTP_SERVER')
        self.port = getenv('PORT')
        self.mail_from = getenv('EMAIL')
        self.password = getenv('PASSWORD')

    def send(self, mail_to: str, name: str,  item: str, return_at: str):
        """
        Sender method
        :param mail_to:
        :type mail_to:
        :param name: borrower name
        :type name: str
        :param item: item name
        :type item: str
        :param return_at:
        :type return_at: str
        """
        subject = f'Please return my {item} !'
        body = Template("""
               Hello $name,
               I hope you return quickly me my $item. 
               The deadline is crossed yesterday ($deadline). 
               Please return my $item because i need this very much. 
               Best regards
               Your Creditor
               """)
        email_ = EmailMessage()
        email_['From'] = self.mail_from
        email_['To'] = mail_to
        email_['Subject'] = subject
        msg = body.substitute(name=name, item=item, deadline=return_at)
        email_.set_content(msg)
        contex = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, int(self.port), context=contex) as smtp:
            smtp.login(self.mail_from, self.password)
            smtp.sendmail(self.mail_from, mail_to, email_.as_string())
