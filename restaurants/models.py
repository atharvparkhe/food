from django.db import models
from base.models import BaseModel
from authentication.models import *
from .manager import FoodModelManager

class RestaurantsModel(BaseModel):
    owner = models.ForeignKey(ShopkeeperModel, related_name="related_shopkeeper", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField(default=-1)
    img = models.ImageField(upload_to="restaurant")
    address = models.TextField()
    pincode = models.CharField(max_length=8)
    latitude = models.CharField(max_length=10, null=True, blank=True)
    longitude = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.name
    def get_menu_items(self):
        return FoodModel.objects.filter(restaurant=self)
    class Meta:
        ordering = ['-created_at']

class FoodCategory(BaseModel):
    food_category = models.CharField(max_length=50)
    def __str__(self):
        return self.food_category

class FoodModel(BaseModel):
    restaurant = models.ForeignKey(RestaurantsModel, related_name="related_restaurant", on_delete=models.CASCADE)
    food_category = models.ForeignKey(FoodCategory, related_name="related_food_type", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=0)
    img = models.ImageField(upload_to="food")
    food_type = models.CharField(choices=(("Veg", "Veg"), ("Non-Veg", "Non-Veg")), default='Veg', max_length=50)
    is_top_selling = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    objects = FoodModelManager()
    admin_objects = models.Manager()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created_at']