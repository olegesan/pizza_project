from django.contrib import admin
from .models import Pizza, Topping, Size,Sub, SubType, PizzaType, Menu
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Size)
admin.site.register(Sub)
admin.site.register(SubType)
admin.site.register(PizzaType)
admin.site.register(Menu)