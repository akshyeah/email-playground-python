from os import name
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  #os path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Akshay kumar'
email['to'] = 'recipient email-ID'
email['subject'] = 'You won a million dollars'

email.set_content(html.substitute({'name':'TInTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender\s email-ID', 'sender\s password')
    smtp.send_message(email)
    print('Email sent successfully!!')
