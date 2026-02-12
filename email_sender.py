from email.message import EmailMessage
import ssl 
import smtplib

email_sender="sumams758@gmail.com"
email_password="gjrs nnwl ccox rahn"

email_receiver='tejebax932@sepole.com'

name='AKshay'
subject="Regarding the learning of Python."
body=f"""As Subject mentioned , I am {name} come up with an amazing opportunity to learn python in my channel it's easy for you learn and develop your skills.
"""
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())
