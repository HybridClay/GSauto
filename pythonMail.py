#From YT "Send Emails With Python [UPDATED]" by Code With Tomi
#First go over to gmail account and setup 2 factor authentication, generate app password
#App passwords > Select app: other(Custom name) > Generate > Copy Code

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'Email_Sender@gmail.com'
email_password = 'Paste Code Here'

email_receiver = "Email_Receiver@gmail.com" #The Clients email address

subject = "Client Name - Balance sheet" #from pdf file name
body = """
Good morning,

Here is your balance sheet

kind regards.

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
    smtp.send_message()

# Note: If you get an SSLCertVerificationError, go YT "How to Send Emails with Python [New Method 2023]" by The PyCoach
#Basically go to Python 3.## folder > double-click on Install Certificate.command > install some certificates


#To add Cc part look into it  "How to send python email with Cc"
# https://stackoverflow.com/questions/1546367/how-to-send-mail-with-to-cc-and-bcc
# Check answer number 74




"""
#From yt "How to Send Emails Using Python - Plain Text, Adding Attachments, HTML Emails, and More" by Corey Schafer
#Using a Local Debug Server:
#In Terminal type: python3 -m smtpd -c DebuggingServer -n localhost:1025
#then you can send emails to this debug Server
Email_Address = "EmailAddress@gmail.com"
Email_Password = "passworHere"

with smtplib.SMTP('localhost', 1025) as smtp:
    subject = 'subjectlineStuffHere'
    body = 'writingStuffinBodyHere'
    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(Email_Address, 'ReceiversEmail@gmail.com', msg)
#Now that message should be printed out in the Temrinal instead of actually sending an email
"""

"""
#Adding Attachments
#For pdf attachment we would do ex:
files = ['file.pdf']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    em.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
"""