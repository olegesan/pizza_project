from django.http import HttpResponse
from django.shortcuts import render
from .models import Size, MenuItem, Category, Kind

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
