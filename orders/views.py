from django.http import HttpResponse, HttpResponseRedirect, QueryDict, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Size, MenuItem, Category, Kind, Cart, Order, Profile, OrderStatus, StatusCatergory, OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import get_messages
from django.contrib import messages
from django.forms.models import model_to_dict
import datetime

#
# authentication content for pages
#

# Create your views here.
def index(request):
    user_info={
    'user': request.user,
    'Auth' : request.user.is_authenticated
    } 
    # print(request.user.user_cart.items.count())  
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
        'toppings': Category.objects.get(addable=True).kinds.all()
    }
    return render(request, "orders/menu.html", content)
'''
signup logic 
'''
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
'''
login logic
'''
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
'''
profile page logic
'''
def profile_open(request, user):
    if request.method=='GET':
        if request.user.is_authenticated and str(request.user) == user:
            content={
                'user' : User.objects.get(username=user),
                'Auth' : request.user.is_authenticated,
                'active': User.objects.get(username=user).profile.orders.filter(status_id=2),
                'order_cat':StatusCatergory.objects.all()
            }
            # print(u.profile.orders.all())
            return render(request,'orders/profile.html', content)
            # return HttpResponse('you are not supposed to be here, bruh')
    #deleteing order logig
    elif request.method == 'DELETE':
        data = QueryDict(request.body)
        username = data['user']
        order_id = data['id']
        # username = request.POST['user']
        # item_id = request.POST['id']
        order = Order.objects.filter(pk=order_id)
        
        order.delete()
        print('Success deleting')
        return HttpResponse(status=200)
        return HttpResponse('you try to DELETE something')

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
            if profile.cart.all().count() > 0:
                total_price = profile.cart.first().total_price()
            else:
                total_price = 0
            content = {
                'user': request.user,
                'orders':profile.orders,
                'name': profile.user,
                'cart': profile.cart.filter(placed=False),
                'Auth': request.user.is_authenticated,
                'total_price': total_price,
            }
            return render(request,'orders/cart.html', content)
    elif request.method == 'POST':
        data = QueryDict(request.body)
        print(data)
        tops = tuple(data['toppings_id'][0:len(data['toppings_id'])-1].split(' '))
        if data['size_id'] == 'false':
            item_id = MenuItem.objects.get(kind = data['kind_id'], category = data['cat_id'])
        else:
            item_id = MenuItem.objects.get(size=data['size_id'], kind = data['kind_id'], category = data['cat_id'])
        username = data['user']
        cart = Cart.objects.create(user_id=User.objects.get(username=username).id, amount = data['amount'], item = item_id, )
        if tops!=('',):
            print(tops)
            cart.toppings.set(tops)
        Profile.objects.get(user_id=User.objects.get(username=username).id).cart.add(cart)        
        # print(cart)
        # cart = Cart.objects.get(user_id=User.objects.get(username=username).id)
        # print('Success adding to the cart')
    elif request.method == 'DELETE':
        data = QueryDict(request.body)
        username = data['user']
        cart_item_id = data['id']
        # username = request.POST['user']
        # item_id = request.POST['id']
        cart_items = Cart.objects.filter(user_id=User.objects.get(username=username).id)
        cart_item = cart_items.get(id=cart_item_id)
        cart_item.delete()
        print('Success deleting')
        return HttpResponse(status=200)
def cart_api(request):
    if request.method == 'GET':
        # cat = Category.objects.get(addable=True).kinds.all() #getting toppings, probably not necessary now
        cat_id, kind_id = request.GET['id'].split('_')
        menu_item = MenuItem.objects.filter(kind = kind_id, category = cat_id)
        toppings=[]
        for topping in Category.objects.get(addable=True).kinds.all():
            toppings.append([topping.kind, topping.id])
        kind= {'cat':Category.objects.get(pk=cat_id).category, 'kind':Kind.objects.get(pk=kind_id).kind,
        'toppings':toppings, 'cat_id':cat_id, 'kind_id':kind_id,'sizes':list(),'toppings_allowed':Kind.objects.get(pk=kind_id).toppings_allowed, 
        'toppings_left':Kind.objects.get(pk=kind_id).toppings_allowed,
        }
        for item in menu_item:
            try:
                if item.size.size:
                    kind[item.size.size] = {'size':item.size.size,
                                    'price': item.price,
                                    'id':item.size.id }
                    kind['sizes'].append(item.size.size)
            except:
                print('error')
        print(kind)
        response = JsonResponse( kind
        )
        return HttpResponse(response, status=200)
#handling orders logic

#addding and deleteing orders in DB
def order_api(request):
    if request.method == 'GET':
        statuses = []
        for status in OrderStatus.objects.all():
            statuses.append([status.status, status.id])
        print(statuses)
        data = {
            'statuses':statuses
        }
        response = JsonResponse(data)
        return HttpResponse(response, status=200)
    if request.method == "UPDATE":
        data = QueryDict(request.body)
        status_id = data['status']
        order_id = data['order_id']
        order = Order.objects.get(pk=order_id)
        order.status_id = status_id
        now = datetime.datetime.now()
        order.date = now
        order.save()
        output ={
            'status':OrderStatus.objects.get(pk=status_id).status,
            'time': now,
            'order_id':order_id,

        }
        response = JsonResponse(output)
        return HttpResponse( response, status=200)
    if request.method == 'POST':
        data = QueryDict(request.body)
        item = data['items'].split()
        username = data['user']
        order = Order.objects.create(user_id=User.objects.get(username=username).id, status_id=2)
        order.item.set(item)
        User.objects.get(username=username).profile.orders.add(order)
        for id in item:
            
            cart = Cart.objects.get(pk=id)
            cart.placed = True
            cart.save()
            print(cart)
        return HttpResponse(status=200)
# managing orders for the staff logic
def order(request):
    if request.user.is_staff:
        content = {
            'orders':Order.objects.all(),
            'user':request.user,
        }
        return render(request, 'orders/orders.html', content)
    else: 
        return render(request, 'orders/index.html')
