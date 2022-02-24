import threading, pdfkit, random, string
from django.conf import settings
from django.core.mail import EmailMessage

def generate_random_string(N):
    result = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    return result

class send_order_email(threading.Thread):
    def __init__(self, email, pdf_file_path):
        self.email = email
        self.pdf_file_path = pdf_file_path
        threading.Thread.__init__(self)
    def run(self):
        try:
            sub = "Order summary"
            body = "Your order summary"
            msg = EmailMessage(sub, body, settings.EMAIL_HOST_USER, [self.email])
            msg.content_subtype = "html"  
            msg.attach_file(self.pdf_file_path)
            print("Email send initiated")
            msg.send()
            print("Email send successfully")
        except Exception as e:
            print(e)

class generate_order_summary(threading.Thread):
    def __init__(self, email_customer, data):
        self.email_customer = email_customer
        self.data = data
        # self.email_shopkeeper = email_shopkeeper
        threading.Thread.__init__(self)
    def run(self):
        try:
            html_file_path = "order_files/html_files/output.html"
            pdf_file_path = "order_files/pdf_files/output" + generate_random_string(5) + ".pdf"
            self.data.to_html(html_file_path)
            pdfkit.from_file(html_file_path, pdf_file_path)
            thread_obj = send_order_email(self.email_customer, pdf_file_path)
            thread_obj.start()
            # thread_obj1 = send_order_email(self.email_shopkeeper, pdf_file_path)
            # thread_obj1.start()
        except Exception as e:
            print(e)