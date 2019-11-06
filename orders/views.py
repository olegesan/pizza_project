from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    content = {
        'reg_pizza':RegularPizza.objects.get(size='large'),
        'toppings': Topping.objects.all(),
        'sic_pizza': SicilianPizza.objects.all(),
        'subs': Sub.objects.all(),
        'sizes':Size.objects.all(),
        'len': [1,2,3]
    }
    return render(request, "orders/index.html", content)
