from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('', views.homePage, name="home"),
	path('about/', views.aboutPage, name="about"),
	path('contact/', views.contactPage, name="contact"),
	path('all-blogs/', views.allBlogsPage, name="all-blogs"),
	path('blog/<blog_id>/', views.blogPage, name="blog"),
	path('add-comment/<blog_id>/', views.add_comment, name="add-comment"),
]