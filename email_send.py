import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('email.html').read_text())

email = EmailMessage()
email['from'] = 'Bokele wakiza franck'
email['to'] = 'exmple@uvatech.com'
email['subject'] = 'You won $1'

email_values = html.substitute({'name':email['from']})
email.set_content(email_values, 'html')


with smtplib.SMTP(host='smt.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'password')
    smtp.send_message(email)
    print('email send')    