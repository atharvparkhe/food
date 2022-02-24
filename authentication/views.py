from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.cache import cache
from .models import *
from .threads import *

@login_required(login_url='/accounts/login/')
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def CustomerSignUp(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            try:
                if CustomerModel.objects.filter(email=email).first():
                    messages.info(request, 'This account already exist. Try logging in.')
                    return redirect('/login')
                else:
                    new_customer = CustomerModel.objects.create(email=email, name=name)
                    new_customer.set_password(password)
                    new_customer.save()
                    messages.info(request, 'We have sent you a verification OTP.\nPlease check your mail.')
                    return redirect('/verify')
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        messages.info(request, 'Something went Wrong')
    return render(request, "accounts/signup.html")


def CustomerVerify(request):
    try:
        if request.method == 'POST':
            otp = request.POST.get('otp')
            try:
                if not cache.get(otp):
                    messages.info(request, 'Invalid OTP')
                else:
                    customer_obj = CustomerModel.objects.get(email = cache.get(otp))
                    if customer_obj:
                        if customer_obj.is_verified:
                            messages.info(request, 'Your profile is already verified.')
                            return redirect('/login')
                        else :
                            customer_obj.is_verified = True
                            customer_obj.save()
                            messages.info(request, 'Your account has been verified. Please Log In')
                            return redirect('/login')
            except Exception as e:
                print(e)
    except Exception as e :
        print(e)
        messages.info(request, 'Something went Wrong')
    return render(request, "accounts/verify.html")


def CustomerLogIn(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            try :
                customer_obj = CustomerModel.objects.filter(email=email).first()
                if customer_obj is None:
                    messages.info(request, 'User does not exists. Please Signup')
                    return redirect('/signup')
                if not customer_obj.is_verified:
                    messages.info(request, 'This profile is not verified. Please Check your mail.')
                    return redirect('/login')    
                try:
                    user = authenticate(email=email, password=password)
                    if user is  None:
                        messages.info(request, 'Incorrect Password.')
                        return redirect('/login')
                    login(request, user)
                    messages.info(request, 'Successfully logged in')
                    return redirect('/')
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        messages.info(request, 'Something went Wrong')
    return render(request, "accounts/login.html")


def CustomerForget(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            if not CustomerModel.objects.get(email=email):
                messages.info(request, 'This user does not exist. Please Signup.')
                return redirect('/signup')
            thread_obj = send_forgot_link(email)
            thread_obj.start()
            messages.info(request, 'We have sent you a link to reset password via mail')
    except Exception as e:
        print(e)
        messages.info(request, 'Something went Wrong')
    return render(request, "accounts/forgot.html")


def CustomerReset(request, token):
    try:
        if not cache.get(token):
            messages.info(request, 'The link has expired')
            return redirect('/login')
        else:
            customer_obj = CustomerModel.objects.get(email = cache.get(token))
            if customer_obj:
                try:
                    if request.method == 'POST':
                        npw = request.POST.get('npw')
                        cpw = request.POST.get('cpw')
                        if npw == cpw:
                            customer_obj.set_password(cpw)
                            customer_obj.save()
                            messages.info(request, 'Password Changed successfully.')
                            return redirect('/login')
                except Exception as e:
                    print(e)
            else:
                messages.info(request, 'User does not exist. Please Signup')
                return redirect('/signup')
    except Exception as e :
        print(e)
        messages.info(request, 'Something went Wrong')
    return render(request, "accounts/reset.html")


def ShopkeeperSignUp(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            aadhar = request.POST.get('aadhar')
            gst = request.POST.get('gst')
            try:
                if ShopkeeperModel.objects.filter(email=email).first():
                    messages.success(request, 'This account already exist. Try logging in.')
                    return redirect('/shopkeeper-login')
                else:
                    new_shopkeeper = ShopkeeperModel.objects.create(
                        email = email,
                        name = name,
                        aadhar_card = aadhar,
                        gst_number = gst
                        )
                    new_shopkeeper.set_password(password)
                    new_shopkeeper.save()
                    messages.info(request, 'We have sent you a verification otp.\nPlease check your mail.')
                    return redirect('/shopkeeper-verify')
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        messages.info(request, 'Something went Wrong')
    return render(request, "accounts/s-signup.html")


def ShopkeeperVerify(request):
    try:
        if request.method == 'POST':
            otp = request.POST.get('otp')
            try:
                if not cache.get(otp):
                    messages.info(request, 'Invalid OTP')
                else:
                    shopkeeper_obj = ShopkeeperModel.objects.get(email = cache.get(otp))
                    if shopkeeper_obj:
                        if shopkeeper_obj.is_verified:
                            messages.info(request, 'Your profile is already verified.')
                            return redirect('/shopkeeper-login')
                        else :
                            shopkeeper_obj.is_verified = True
                            shopkeeper_obj.save()
                            messages.info(request, 'Your account has been verified. Please Log In')
                            return redirect('/shopkeeper-login')
            except Exception as e:
                print(e)
    except Exception as e :
        print(e)
        messages.info(request, 'Something went Wrong')
    return render(request, "accounts/s-verify.html")


def ShopkeeperLogIn(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            try :
                shopkeeper_obj = ShopkeeperModel.objects.filter(email=email).first()
                if shopkeeper_obj is None:
                    messages.info(request, 'User does not exists. Please Signup')
                    return redirect('/shopkeeper-signup')
                if not shopkeeper_obj.is_verified:
                    messages.info(request, 'This profile is not verified. Please Check your mail.')
                    return redirect('/shopkeeper-login')
                try:
                    user = authenticate(email=email, password=password)
                    if user is None:
                        messages.info(request, 'Incorrect Password')
                        return redirect('/shopkeeper-login')
                    login(request, user)
                    from restaurants.models import RestaurantsModel
                    if RestaurantsModel.objects.filter(owner = shopkeeper_obj).exists():
                        return redirect('dashboard')
                    else:
                        return redirect('add-restaurant')            
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
        messages.info(request, 'Something went Wrong')
    return render(request, "accounts/s-login.html")


def ShopkeeperForget(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            if ShopkeeperModel.objects.get(email=email) == None:
                messages.info(request, 'This user does not exist. Please Signup.')
                return redirect('/shopkeeper-signup')
            else :
                send_forgot_link(email)
                messages.info(request, 'We have sent you a link to reset password via mail')
    except Exception as e:
        print(e)
        messages.info(request, 'Something went Wrong')
    return render(request, "accounts/s-forgot.html")


def ShopkeeperReset(request, token):
    try:
        if not cache.get(token):
            messages.info(request, 'The link has expired')
            return redirect('shopkeeper-login')
        else:
            shopkeeper_obj = ShopkeeperModel.objects.get(email = cache.get(token))
            if shopkeeper_obj:
                try:
                    if request.method == 'POST':
                        shopkeeper_obj.set_password(request.POST.get('s_pw'))
                        shopkeeper_obj.save()
                        messages.info(request, 'Password Changed successfully.')
                        return redirect('/login')
                except Exception as e:
                    print(e)
            else:
                messages.info(request, 'User does not exist. Please Signup')
                return redirect('/shopkeeper-signup')
    except Exception as e :
        print(e)
        messages.info(request, 'Something went Wrong')
    return render(request, "accounts/s-reset.html")