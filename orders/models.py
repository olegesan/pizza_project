from django.db import models
###
### support 
###
class  Size(models.Model):
    size = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.size}"
class Price(models.Model):
    price = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.price}"
    class Meta:
        ordering = ['price']
class Kind(models.Model):
    kind = models.CharField(max_length=64)
    def __str__(self):
        return f'{self.kind}'
class Category(models.Model):
    category =  models.CharField(max_length=64)
    def __str__(self):
        return f'{self.category}'
class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="sizes", blank = True, null = True)
    price = models.ForeignKey(Price, on_delete=models.CASCADE, related_name='prices', blank = True, null = True)
    kind = models.ForeignKey(Kind,on_delete=models.CASCADE, related_name='kinds')
    def __str__(self):
        if str(self.category) !='Toppings':
            return f'{self.category}: {self.kind} {self.size} for ${self.price} dollars'
        return f'{self.category}: {self.kind}'
    class Meta:
        ordering = ['-category', 'price', 'size']


    










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
    
