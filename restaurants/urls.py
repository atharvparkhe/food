from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('all-restaurants/', views.allRestaurants, name="all-restaurants"),
	path('restaurant/<restaurant_id>/', views.allProducts, name="restaurant"),
	path('restaurant/item/<product_id>/', views.product, name="product"),

	path('shopkeeper/dashboard/', views.dashboard, name="dashboard"),
	path('shopkeeper/all-products/', views.shopProducts, name="all-products"),
	path('shopkeeper/product/<product_id>/', views.sellProduct, name="product"),
	path('shopkeeper/new-product/', views.newProduct, name="new-product"),
	path('shopkeeper/product/edit-product/<product_id>/', views.editProduct, name="edit-product"),
	path('shopkeeper/product/delete-product/<product_id>/', views.deleteProduct, name="delete-product"),

	path('shopkeeper/add-restaurant/', views.addRestaurant, name="add-restaurant"),
	path('shopkeeper/orders/', views.orders, name="orders"),
	path('shopkeeper/profile/', views.profile, name="profile"),
]