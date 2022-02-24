from django.contrib import admin
from .models import *

class FoodModelAdmin(admin.StackedInline):
    model = FoodModel
    fk_name = 'restaurant'

@admin.register(RestaurantsModel)
class RestaurantsModelAdmin(admin.ModelAdmin):
    inlines = [ FoodModelAdmin ]

admin.site.register(FoodCategory)
admin.site.register(FoodModel)
# admin.site.register(RestaurantsModel)