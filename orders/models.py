from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

###
### support 
###
class  Size(models.Model):
    size = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.size}"
    class Meta:
        ordering = ['-size']
class Kind(models.Model):
    kind = models.CharField(max_length=64)
    menu_priority = models.IntegerField(default = 100)
    toppings_allowed = models.IntegerField(default = 0)
    def __str__(self):
        return f'{self.kind}'
    class Meta:
        ordering = ['-menu_priority']
class Category(models.Model):
    category =  models.CharField(max_length=64)
    sizes = models.ManyToManyField(Size, related_name="cat_sizes", blank = True, null = True)
    kinds = models.ManyToManyField(Kind, related_name='cat_kinds', blank = False)
    menu_priority = models.IntegerField(default = 100)
    no_price=models.BooleanField(default=False)
    toppings = models.BooleanField(default=False)
    addable = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.category}'
    def show_sizes(self):
        return f'{self.sizes.all()}'
    class Meta:
        ordering = ['menu_priority']
class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories", blank = True, null = True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="sizes", blank = True, null = True)
    price = models.FloatField(blank=True, null = True)
    kind = models.ForeignKey(Kind,on_delete=models.CASCADE, related_name='kinds')
    menu_priority = models.IntegerField(default = 100)
    def __str__(self):
        if str(self.category) != 'Toppings':
            return f'{self.category}: {self.kind} {self.size} for ${self.price} dollars'
        return f'{self.category}: {self.kind}'
    class Meta:
        ordering = ['-category', 'price', 'size']

"""
ordering system
"""

class OrderStatus(models.Model):
    status = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.status}"
class Cart(models.Model):
    item = models.ForeignKey(MenuItem,on_delete=models.CASCADE, related_name='cart_items', null=True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='user_cart', blank = False, null = False)
    amount = models.IntegerField()
    toppings = models.ManyToManyField(Kind, blank = True, related_name = 'cart_topings')
    def __str__(self):
        return f"User: {self.user} Cart item: {self.item} "
class Order(models.Model):
    item = models.ManyToManyField(Cart, related_name='order_items')
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='user_order', blank = False, null = False)
    status = models.ForeignKey(OrderStatus,on_delete = models.CASCADE, related_name='order_statuses', blank = False, null = False)
    def __str__(self):
        return f'User: {self.user} content: {self.item} status: {self.status}'

'''
profile system
'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=256, blank=True)
    orders = models.ManyToManyField(Order, related_name='users_order', blank = True)
    firstname = models.CharField(max_length=64, blank = True)
    lastname = models.CharField(max_length=64, blank = True)
    carts = models.ManyToManyField(Cart, related_name='users_carts', blank = True)
    def __str__(self):
        return f'{self.user}'
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

   
# class Pizza(MenuItem):
#     def __str__(self):
#         return f'{self.category} {self.size} {self.price} {self.kind}'

    










# ''' 
# general models
# '''
# # class Menu(models.Model):
# #     options = (('Y', 'Yes'),('N',"No"))
# #     listed = models.CharField(choices=options, max_length=5)
# #     def __str__(self):
# #         return f'{self.listed}'
# class Size(models.Model):
#     size = models.CharField(max_length=64)
#     def __str__(self):
#         return self.size

# ''' 
# pizza related section
# '''
# # class PizzaType(models.Model):
# #         pizza_type = models.CharField(max_length=128)
# #         def __str__(self):
# #             return self.pizza_type
# class Topping(models.Model):
#     topping = models.CharField(max_length=128)
#     def __str__(self):
#         return f'{self.topping}'
# class RegularPizza(models.Model):
#     types = (("Cheese", 'Cheese'),('1 topping','1 topping'),('2 toppings','2 toppings'),('3 toppings','3 toppings'), ('special','special'))
#     pizza_type = models.CharField(choices=types, max_length=64)
#     size = models.ForeignKey(Size, on_delete=models.CASCADE,related_name='reg_pizza_sizes')
#     # toppings = models.ManyToManyField(Topping, blank=True, related_name='reg_pizza_topings', null=True)
#     price = models.CharField(max_length=64)
#     # on_the_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_pizzas')
#     name = 'Regular Pizza'
#     class Meta:
#         ordering = ['price'] 
#     def __str__(self):
#         return f'{self.size} {self.pizza_type} pizza for ${self.price} dollars'
# class SicilianPizza(models.Model):
#     types = (("Cheese",'Cheese'),('1 item','1 item'),('2 items','2 items'),('3 items','3 items'), ('special','special'))
#     pizza_type = models.CharField(choices=types, max_length=64)
#     size = models.ForeignKey(Size, on_delete=models.CASCADE,related_name='sic_pizza_sizes')
#     # toppings = models.ManyToManyField(Topping, blank=True, related_name='sic_pizza_topings')
#     price = models.CharField(max_length=64)
#     # on_the_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_pizzas')
#     name = 'Sicilian Pizza'
#     class Meta:
#         ordering = ['price'] 
#     def __str__(self):
#         return f'{self.size} {self.pizza_type} pizza for ${self.price} dollars'
# '''
# sub related models
# '''
# class SubType(models.Model):
#         sub_type = models.CharField(max_length=128)
#         def __str__(self):
#             return self.sub_type
# class Sub(models.Model):
#     sub_type = models.ForeignKey(SubType, on_delete=models.CASCADE, related_name='sub_types')
#     size = models.ForeignKey(Size, on_delete=models.CASCADE,related_name='sub_sizes')
#     price = models.CharField(max_length=64)
#     # listed = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_subs')
#     name ='Sub'
#     class Meta:
#         ordering = ['price'] 
#     def __str__(self):
#         return f'{self.size} {self.sub_type} for {self.price}'
# '''
# menu realted section
# '''
# # class MenuItem(models.Model): 
# #     type_item = models.CharField(max_length=64)
# # class Menu(models.Model):
# #     item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, blank = True)
# # class Pizza(MenuItem):
# #     name = models.CharField(max_length=64)
    
