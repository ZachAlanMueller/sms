import os
import sys
import json
import smtplib
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))


carriers = {
    'att':    '@mms.att.net',
    'tmobile':' @tmomail.net',
    'verizon':  '@vtext.com',
    'sprint':   '@page.nextel.com'
}

def send(message):

    to_number = '000-000-0000{}'.format(carriers['att'])
    auth = (os.getenv("EMAIL"), os.getenv("PASSWORD"))

    #Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(auth[0], auth[1])

    # Send text message through SMS gateway of destination number
    server.sendmail( auth[0], to_number, message)

send('test')