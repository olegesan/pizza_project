from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Size, MenuItem, Category, Kind
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'orders/index.html')
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
def signup(request):
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
