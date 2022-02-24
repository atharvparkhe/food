from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('add-to-cart/<item_id>/', views.add_to_cart, name="add-to-cart"),
	path('remove-from-cart/<item_id>/', views.remove_from_cart, name="remove-from-cart"),
	path('delete-from-cart/<item_id>/', views.delete_from_cart, name="delete-from-cart"),
	path('cart/apply-coupon/<cart_id>/', views.couponApplied, name="apply-coupon"),

	path('success/', views.success, name="success"),
	path('failed/', views.failed, name="failed"),
]