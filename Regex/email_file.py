import os, datetime
import smtplib
from email.message import EmailMessage

email = os.environ.get('EMAIL')
password = os.environ.get('EMAIL_PASSWORD') 


def sending_email(dictionary_of_people, sender, recipient, excel_attachment):
    current_date = datetime.date.today()
    
    message = EmailMessage()
    message['Subject'] = f'A list of people from {current_date}'
    message['From'] = sender
    message['To'] = recipient
    message.set_content(f'''Dear Rafał,
enclosed you will find an excel file "people" from {current_date} with {len(dictionary_of_people)} people.

Best Regards''')
    
    with open(excel_attachment, 'rb') as f:
        file_data = f.read()
    message.add_attachment(file_data, maintype="application", subtype="xlsx", filename=excel_attachment)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email, password)
        smtp.send_message(message)