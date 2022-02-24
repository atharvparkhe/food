from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .manager import CouponManager
from django.db import models
from base.models import BaseModel
from authentication.models import CustomerModel
from restaurants.models import *


class Coupons(BaseModel):
    coupon_name = models.CharField(max_length=100, unique=True)
    coupon_discount_amount = models.FloatField(default=20)
    use_times = models.PositiveIntegerField(default=10)
    is_deleted = models.BooleanField(default=False)
    objects = CouponManager()
    admin_objects = models.Manager()
    def __str__(self):
        return self.coupon_name

class CartModel(BaseModel):
    owner = models.ForeignKey(CustomerModel, related_name="related_customer_cart",on_delete=models.PROTECT)
    is_paid = models.BooleanField(default=False)
    coupon_applied = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    total_amt = models.FloatField(default=0)
    order_id = models.CharField(max_length=100, null=True, blank=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True)
    payment_signature = models.CharField(max_length=100, null=True, blank=True)

class CartItems(BaseModel):
    owner = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name="related_customer_cart_items")
    cart = models.ForeignKey(CartModel, related_name="related_cart", on_delete=models.CASCADE)
    item = models.ForeignKey(FoodModel, related_name="related_items", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0)


@receiver(pre_save, sender=CartItems)
def get_total_amt(sender, instance, *args, **kwargs):
    instance.total = instance.item.price * instance.quantity

@receiver(post_save, sender=CartItems)
def get_total_amt(sender, instance, *args, **kwargs):
    total=0
    cart_obj = CartModel.objects.get(owner = instance.owner, is_paid=False)
    for i in CartItems.objects.filter(cart=cart_obj):
        total += i.total
    cart_obj.total_amt = total
    cart_obj.save()

@receiver(pre_save, sender=Coupons)
def coupon_update(sender, instance, *args, **kwargs):
    instance.use_times -= 1
    if instance.use_times < 1:
        instance.is_deleted = True