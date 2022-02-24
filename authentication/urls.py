from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('login/', views.CustomerLogIn, name="login"),
	path('signup/', views.CustomerSignUp, name="signup"),
	path('verify/', views.CustomerVerify, name="verify"),
	path('forgot/', views.CustomerForget, name="forgot"),
	path('reset/<token>/', views.CustomerReset, name="reset"),

	path('logout/', views.logoutView, name="logout"),

    path('shopkeeper-login/', views.ShopkeeperLogIn, name="shopkeeper-login"),
	path('shopkeeper-signup/', views.ShopkeeperSignUp, name="shopkeeper-signup"),
	path('shopkeeper-verify/', views.ShopkeeperVerify, name="shopkeeper-verify"),
	path('shopkeeper-forgot/', views.ShopkeeperForget, name="shopkeeper-forgot"),
	path('shopkeeper-reset/<token>/', views.ShopkeeperReset, name="shopkeeper-reset"),
]