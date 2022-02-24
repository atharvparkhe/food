from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from cart.models import *
from .models import *

def allRestaurants(request):
    restaurants = RestaurantsModel.objects.all()
    return render(request, 'restaurants/all-restaurants.html', {'restaurants': restaurants})

def allProducts(request, restaurant_id):
    items = FoodModel.objects.filter(restaurant = RestaurantsModel.objects.get(id=restaurant_id))
    categories = FoodCategory.objects.all()
    context = {
        "items":items,
        "categories":categories,
    }
    return render(request, 'restaurants/restaurant-items.html', context)

def product(request, product_id):
    item = FoodModel.objects.get(id=product_id)
    similar_obj = FoodModel.objects.filter(restaurant = item.restaurant).exclude(id=product_id)
    context = {
        'item': item,
        'similar_obj': similar_obj,
    }
    return render(request, 'restaurants/item.html', context)


@login_required(login_url='/shopkeeper-login/')
def dashboard(request):
    context = {}
    try:
        user_obj = ShopkeeperModel.objects.get(email=request.user)
        restaurant_obj = RestaurantsModel.objects.get(owner=user_obj)
        context["restaurant_obj"] = restaurant_obj
        order_objs = CartItems.objects.filter(item__restaurant=restaurant_obj, cart__is_paid=True)
        context["order_objs"] = order_objs
    except Exception as e:
        print(e)
    return render(request, 'shopkeeper/dashboard.html',  context)

@login_required(login_url='/shopkeeper-login/')
def shopProducts(request):
    context = {}
    try:
        user_obj = ShopkeeperModel.objects.get(email=request.user)
        restaurant_obj = RestaurantsModel.objects.get(owner=user_obj)
        product_obj = FoodModel.objects.filter(restaurant = restaurant_obj)
        context["product_obj"] = product_obj
        context["restaurant_obj"] = restaurant_obj
    except Exception as e:
        print(e)
    return render(request, 'shopkeeper/all-products.html', context)

@login_required(login_url='/shopkeeper-login/')
def sellProduct(request, product_id):
    context = {}
    try:
        user_obj = ShopkeeperModel.objects.get(email=request.user)
        restaurant_obj = RestaurantsModel.objects.get(owner=user_obj)
        product_obj = FoodModel.objects.get(id = product_id)
        context["product_obj"] = product_obj
        context["restaurant_obj"] = restaurant_obj
    except Exception as e:
        print(e)
    return render(request, 'shopkeeper/product.html', context)

@login_required(login_url='/shopkeeper-login/')
def editProduct(request, product_id):
    context = {}
    try:
        user_obj = ShopkeeperModel.objects.get(email=request.user)
        restaurant_obj = RestaurantsModel.objects.get(owner=user_obj)
        product_obj = FoodModel.objects.get(id = product_id)
        context["food_category"] = FoodCategory.objects.all()
        context["product_obj"] = product_obj
        context["restaurant_obj"] = restaurant_obj
        if request.method == 'POST':
            product_obj.name = request.POST.get("name")
            product_obj.price = request.POST.get("price")
            product_obj.description = request.POST.get("desc")
            product_obj.food_category_id = FoodCategory.objects.get(id=request.POST.get("food_category_id"))
            product_obj.img = request.FILES.get("img")
            product_obj.save()
            return redirect("all-products")
    except Exception as e:
        print(e)
    return render(request, 'shopkeeper/edit-product.html', context)

@login_required(login_url='/shopkeeper-login/')
def newProduct(request):
    context = {}
    try:
        context["food_category"] = FoodCategory.objects.all()
        user_obj = ShopkeeperModel.objects.get(email=request.user)
        restaurant_obj = RestaurantsModel.objects.get(owner=user_obj)
        FoodModel.objects.create(
            restaurant = restaurant_obj,
            food_category = FoodCategory.objects.get(id=request.POST.get("food_category_id")),
            name = request.POST.get("name"),
            description = request.POST.get("desc"),
            price = request.POST.get("price"),
            img = request.FILES.get("img"),
            food_type = request.POST.get("type")
        )
        return redirect("all-products")
    except Exception as e:
        print(e)
    return render(request, 'shopkeeper/new-product.html', context)

@login_required(login_url='/shopkeeper-login/')
def deleteProduct(request, product_id):
    if FoodModel.objects.filter(id = product_id).exists() :
        product_obj = FoodModel.objects.get(id = product_id)
        product_obj.is_deleted = True
        product_obj.save()
        return redirect("all-products")
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/shopkeeper-signup/')
def addRestaurant(request):
    try:
        user_obj = ShopkeeperModel.objects.get(email=request.user)
        RestaurantsModel.objects.create(
            owner = user_obj,
            name = request.POST.get("name"),
            description = request.POST.get("desc"),
            img = request.FILES.get("img"),
            address = request.POST.get("address"),
            pincode = request.POST.get("pincode"),
        )
        print("restaurant created !")
        return redirect("all-products")
    except Exception as e:
        print(e)
    return render(request, 'shopkeeper/add-restaurant.html')

@login_required(login_url='/shopkeeper-login/')
def orders(request):
    return render(request, 'shopkeeper/orders.html')

@login_required(login_url='/shopkeeper-login/')
def profile(request):
    return render(request, 'shopkeeper/profile.html')