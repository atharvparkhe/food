from django.contrib import admin
from .models import *

admin.site.register(ShopkeeperModel)
admin.site.register(CustomerModel)
admin.site.register(CustomerAddress)