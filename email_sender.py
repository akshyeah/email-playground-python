import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Akkii'
email['to'] = 'akhilkumar261999@gmail.com'
email['subject'] = 'You won a million dollars'

email.set_content('I am a python dev!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('akshay19996@gmail.com', '96.attitude.19')
    smtp.send_message(email)
    print('Email sent successfully!!')