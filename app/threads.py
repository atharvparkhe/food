import threading
from django.conf import settings
from django.core.mail import send_mail

class send_email(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "Thanks fo filling the contact form."
            message = "We will reach out to you as soon as possible.\nThank you."
            email_from = settings.EMAIL_HOST_USER
            print("Email send started")
            send_mail(subject , message ,email_from ,[self.email])
            print("Email send finished")
        except Exception as e:
            print(e)