from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from base.models import *
from .threads import *

class ShopkeeperModel(BaseUser):
    aadhar_card = models.CharField(max_length=16, unique=True)
    gst_number = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'shopkeeper'

class CustomerModel(BaseUser): 
    newsletter = models.BooleanField(default=False)
    def __str__(self):
        return self.email
    def get_cart(self):
        try:
            cart = self.related_customer_cart.filter(is_paid=False)
            return cart
        except Exception as e:
            return False
    class Meta:
        db_table = 'customer'

class CustomerAddress(BaseModel):
    customer = models.ForeignKey(CustomerModel, related_name="customer_address", on_delete=models.CASCADE)
    address = models.TextField()
    pincode = models.CharField(max_length=100)
    landmark = models.CharField(max_length=50)


@receiver(post_save, sender=ShopkeeperModel)
def send_mail(sender,instance,created, **kwargs):
    if created:
        emailID = instance.email
        thread_obj = send_verification_otp(emailID)
        thread_obj.start()

@receiver(post_save, sender=CustomerModel)
def send_mail(sender,instance,created, **kwargs):
    if created:
        emailID = instance.email
        thread_obj = send_verification_otp(emailID)
        thread_obj.start()