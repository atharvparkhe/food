from authentication.models import CustomerModel
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.conf import settings
from decouple import config
from restaurants.models import *
from .threads import *
from .models import *
import razorpay, pandas

client = razorpay.Client(auth=(config("PUBLIC_KEY"), config("PRIVATE_KEY")))


@login_required(login_url='/login/')
def add_to_cart(request, item_id):
    try:
        customer = CustomerModel.objects.get(email=request.user)
        food_obj = FoodModel.objects.get(id=item_id)
        cart_obj, _ = CartModel.objects.get_or_create(owner=customer, is_paid=False)
        if cart_obj.related_cart.filter(item=food_obj).exists():
            cart_item = CartItems.objects.get(cart=cart_obj, item=food_obj)
            cart_item.quantity += 1
            cart_item.save()
        else : 
            CartItems.objects.create(owner=customer ,cart=cart_obj, item=food_obj)
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login/')
def remove_from_cart(request, item_id):
    try:
        customer = CustomerModel.objects.get(email=request.user)
        food_obj = FoodModel.objects.get(id = item_id)
        cart_obj = CartModel.objects.get(owner = customer, is_paid = False)
        if cart_obj.related_cart.filter(item=food_obj).exists():
            cart_item = CartItems.objects.get(cart = cart_obj, item = food_obj)
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.quantity -= 1
                cart_item.save()
                cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login/')
def delete_from_cart(request, item_id):
    try:
        customer = CustomerModel.objects.get(email=request.user)
        food_obj = FoodModel.objects.get(id = item_id)
        cart_obj = CartModel.objects.get(owner = customer, is_paid = False)
        if cart_obj.related_cart.filter(item=food_obj).exists():
            cart_item = CartItems.objects.get(cart = cart_obj, item = food_obj)
            cart_item.quantity = 0
            cart_item.save()
            cart_item.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login/')
def cart(request):
    user = CustomerModel.objects.get(email=request.user)
    if CartModel.objects.filter(owner=user, is_paid=False).exists():
        cart_obj = CartModel.objects.get(owner=user, is_paid=False)
        items_obj = CartItems.objects.filter(cart=cart_obj)
        return render(request, 'orders/cart.html', {"items_obj":items_obj, "cart_obj":cart_obj})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/login/')
def checkout(request):
    context = {}
    try:
        user = CustomerModel.objects.get(email=request.user)
        cart_obj = CartModel.objects.get(owner=user, is_paid=False)
        items_obj = CartItems.objects.filter(cart=cart_obj)
        amt=cart_obj.total_amt * 100
        address = CustomerAddress.objects.filter(customer=user)
        payment = client.order.create({
            'amount' :  amt,
            'currency' : 'INR' ,
            'payment_capture' : 1 
        })
        cart_obj.order_id = payment['id']
        cart_obj.save()
        context["items_obj"] = items_obj
        context["cart_obj"] = cart_obj
        context["address"] = address
        context["key"] = config("PUBLIC_KEY")
        context["order_id"] = payment['id']
    except Exception as e:
        print(e)
    return render(request, 'orders/checkout.html', context)

@login_required(login_url='/login/')
def success(request):
    context = {}
    try:
        user = CustomerModel.objects.get(email=request.user)
        cart_obj = CartModel.objects.get(owner=user, is_paid=False)
        items_obj = CartItems.objects.filter(cart=cart_obj)
        context["items_obj"] = items_obj
        data, data2 = [], []
        for obj in items_obj:
            mylist = [obj.item.name, obj.item.price, obj.quantity, obj.total]
            data.append(mylist)
            # mylist2 = [obj.item.name, obj.quantity, user.email, ]
            # data2.append(mylist2)
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(obj.item.restaurant.owner.email)
            # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        data = pandas.DataFrame(data, columns= [ 'Items', 'Price', 'Quantity', 'Total'] )
        thread_obj = generate_order_summary(request.user, data)
        thread_obj.start()
        cart_obj.order_id = request.GET.get('razorpay_order_id')
        cart_obj.payment_id = request.GET.get('razorpay_payment_id')
        cart_obj.payment_signature = request.GET.get('razorpay_signature') 
        cart_obj.is_paid = True
        cart_obj.save()
    except Exception as e:
        print(e)
    return render(request, 'orders/success.html', context)

@login_required(login_url='/login/')
def failed(request):
    return render(request, 'orders/failed.html')

@login_required(login_url='/login/')
def couponApplied(request, cart_id):
    cart_obj = CartModel.objects.get(id = cart_id)
    if request.method == 'POST':
        name = request.POST.get("coupon")
        if Coupons.objects.filter(coupon_name = name).exists() and cart_obj.coupon_applied == False:
            coupon_obj = Coupons.objects.get(coupon_name = request.POST.get("coupon"))
            cart_obj.total_amt -= cart_obj.total_amt*coupon_obj.coupon_discount_amount
            cart_obj.coupon_applied = True
            cart_obj.save()
            coupon_obj.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else :
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))