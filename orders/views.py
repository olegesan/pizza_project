from django.http import HttpResponse
from django.shortcuts import render
from .models import Size, MenuItem, Category, Price, Kind

# Create your views here.
def index(request):
    content = {
        "menu": MenuItem.objects.all(),
        'categories':Category.objects.all(),
        'sizes': Size.objects.all(),
    }
    return render(request, "orders/index.html", content)
