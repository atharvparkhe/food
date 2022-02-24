from django.contrib import admin
from . models import *

class CartModelAdmin(admin.ModelAdmin):
    list_display = ['owner' , 'is_paid' ,'total_amt']
    
admin.site.register(CartModel,CartModelAdmin)

class CartItemsAdmin(admin.ModelAdmin):
    list_display = ['item','quantity','total']

admin.site.register(CartItems, CartItemsAdmin)

admin.site.register(Coupons)