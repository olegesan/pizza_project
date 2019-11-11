from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Size, MenuItem, Category, Kind
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    content = {
        'user': request.user,
        'Auth' : request.user.is_authenticated
    }
    return render(request, 'orders/index.html', content)
def menu(request):
    content = {
        "menu": MenuItem.objects.all(),
        'categories':Category.objects.all(),
        'sizes': Size.objects.all(),
        'menu_raw' : MenuItem.objects,
        'kinds': Kind.objects.all()
    }
    return render(request, "orders/menu.html", content)
def somewhere(request):
    return HttpResponse('Somewhere')
def signup_page(request):
    return render(request,'orders/signup.html')
def signup_new(request):
    try:
        # print(reuqest.POST['email'])
        username = request.POST['login']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username,
                                    email,
                                    password)
        user.save()
    except:
        # print(email, password, username)
        return HttpResponse('there was an error')
    return HttpResponseRedirect('/')
def login_func(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request,'orders/index.html', {'message':'success!'}) 
    except:
        return HttpResponse('something went suuuper wrong')
def login_page(request):
    return render(request,'orders/login.html')
# def profile_open(request, user_id):
#     content={
#         'user' = User.objects.get(pk=)
#     }
#     return render(request,'orders/profile.html')