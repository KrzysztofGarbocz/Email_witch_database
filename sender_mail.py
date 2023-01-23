import ssl
import smtplib
from email.message import EmailMessage
from os import environ, getenv
from dotenv import load_dotenv
load_dotenv()

print(environ)
