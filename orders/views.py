from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Size, MenuItem, Category, Kind, Cart, Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import get_messages
from django.contrib import messages

#
# authentication content for pages
#

# Create your views here.
def index(request):
    user_info={
    'user': request.user,
    'Auth' : request.user.is_authenticated
    }   
    return render(request, 'orders/index.html', user_info)
def menu(request):
    content = {
        "menu": MenuItem.objects.all(),
        'categories':Category.objects.all(),
        'sizes': Size.objects.all(),
        'menu_raw' : MenuItem.objects,
        'kinds': Kind.objects.all(),
        'user': request.user,
        'Auth' : request.user.is_authenticated,
    }
    return render(request, "orders/menu.html", content)
def signup(request):
    if request.method == 'GET':
        return render(request,'orders/signup.html')
    elif request.method == 'POST':
        username = request.POST['login']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username,
                                    email,
                                    password)
        user.profile.firstname = request.POST['firstname']
        user.profile.lastname = request.POST['lastname']
        user.profile.address = request.POST['address']
        user.save()
        return redirect('/')
    # except:
    #     # print(email, password, username)
    #     return HttpResponse('there was an error')
    return redirect('/')
def login_func(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR, 'Incorrect login or password')
            return redirect(request,'orders/login.html')
    except:
        return render(request,'orders/login.html', {'message':'Incorrect login or password'}) 
def login_page(request):
    return render(request,'orders/login.html')
def logout_page(request):
    user_info={
    'user': request.user,
    'Auth' : request.user.is_authenticated,
    }
    return render(request,'orders/logout.html', user_info)
def logout_func(request):
    try:
        logout(request)
        return render(request,'orders/index.html')
    except:
        return HttpResponse('something went suuuper wrong, perhaps you were not logged in')

def profile_open(request, user):
    try:
        if request.user.is_authenticated and str(request.user) == user:
            content={
                'user' : User.objects.get(username=user),
                'Auth' : request.user.is_authenticated
            }
            u = User.objects.get(username=user)
            print(u.profile.firstname)
            return render(request,'orders/profile.html', content)
        else:
            return HttpResponse('you are not supposed to be here, bruh')
    except:
        return HttpResponse('you are not supposed to be here, bruh')

def profile_edit(request, user):
    if request.method == "GET":
        context = {
            'user': User.objects.get(username=user),
            'Auth' : request.user.is_authenticated,
        }
        return render(request,'orders/profile_edit.html', context )
    elif request.method == "POST":
        user = User.objects.get(username=user)
        user.profile.firstname = request.POST['firstname']
        user.profile.lastname = request.POST['lastname']
        user.profile.address = request.POST['address']
        user.save() 
        return HttpResponseRedirect(reverse('profile', args=(user,)))
    else:
        return HttpResponse('something else hapepend')
'''
cart system and orders
'''
def cart(request, user):
    if request.method == "GET":
        if request.user.is_authenticated:
            profile = User.objects.get(username=user).profile
            content = {
                'user': request.user,
                'orders':profile.orders,
                'name': profile.user,
                'cart': Cart.objects.get(user_id=profile.user.id),
            }
            return render(request,'orders/cart.html', content)
    elif request.method == 'POST':
        username = request.POST['user']
        item_id = request.POST['id']
        cart = Cart.objects.get(user_id=User.objects.get(username=username).id)
        # print(username, item_id)
        cart.items.add(item_id)
        