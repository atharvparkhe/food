from django.db.models.fields import EmailField
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from authentication.models import *
from restaurants.models import *
from .models import *
from .threads import *

def homePage(request):
    context = {}
    try:
        print(request.user)
        blog_obj = BlogModel.objects.all()
        rest_obj = RestaurantsModel.objects.all()
        food_obj = FoodModel.objects.filter(is_top_selling=True)
        context["blog_obj"] = blog_obj
        context["rest_obj"] = rest_obj
        context["food_obj"] = food_obj
    except Exception as e:
        print(e)
    return render(request, "main/home.html", context)

def aboutPage(request):
    return render(request, "main/about.html")

def contactPage(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            msg = request.POST.get("message")
            customer, _ = CustomerModel.objects.get_or_create(email=email)
            ContactUs.objects.create(user=customer, message=msg)
            thread_obj = send_email(email)
            thread_obj.start()
            return redirect('/home')
    except Exception as e:
        print(e)
    return render(request, "main/contact.html")

def allBlogsPage(request):
    try:
        blog_obj = BlogModel.objects.all()
    except Exception as e:
        print(e)
    return render(request, "main/all-blogs.html", {"blog_obj":blog_obj})

def blogPage(request, blog_id):
    context = {}
    try:
        all_blog = BlogModel.objects.all().exclude(id=blog_id)
        blog_obj = BlogModel.objects.get(id=blog_id)
        comment_obj = BlogCommentsModel.objects.filter(blog=blog_obj)
        context["blog_obj"] = blog_obj
        context["comment_obj"] = comment_obj
        context["all_blog"] = all_blog
    except Exception as e:
        print(e)
    return render(request, "main/blog.html", context)

@login_required(login_url='/login/')
def add_comment(request, blog_id):
    try:
        blog_obj = BlogModel.objects.get(id=blog_id)
        BlogCommentsModel.objects.create(
            blog=blog_obj,
            comment=request.POST.get("comment"),
            commenter=BaseUser.objects.get(email=request.user)
        )
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def subscribe(request):
    try:
        if request.method == "POST":
            email = request.POST.get("email")
            obj, _ = CustomerModel.objects.get_or_create(email=email)
            obj.newsletter = True
            obj.save()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def unsubscribe(request, email):
    try:
        obj = CustomerModel.objects.get(email=email)
        obj.newsletter = False
        obj.save()
    except Exception as e:
        print(e)
    return render(request, "main/unsubscribe.html")