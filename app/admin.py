from django.contrib import admin
from .models import *

admin.site.register(BlogModel)
admin.site.register(BlogCommentsModel)
admin.site.register(ContactUs)