from django.contrib import admin
from .models import RegularPizza, SicilianPizza, Topping, Size,Sub, SubType
# Register your models here.
admin.site.register(SicilianPizza)
admin.site.register(RegularPizza)
admin.site.register(Topping)
admin.site.register(Size)
admin.site.register(Sub)
admin.site.register(SubType)
# admin.site.register(PizzaType)
# admin.site.register(Menu)
# admin.site.register(Pizza)
# admin.site.register(MenuItem)
#  MenuItem, Menu, Pizza
