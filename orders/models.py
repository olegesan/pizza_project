from django.db import models

''' 
general models
'''
class Menu(models.Model):
    options = (('Y', 'Yes'),('N',"No"))
    listed = models.CharField(choices=options, max_length=5)
    def __str__(self):
        return f'{self.listed}'
class Size(models.Model):
    size = models.CharField(max_length=64)
    def __str__(self):
        return self.size

''' 
pizza related section
'''
class PizzaType(models.Model):
        pizza_type = models.CharField(max_length=128)
        def __str__(self):
            return self.pizza_type
class Topping(models.Model):
    topping = models.CharField(max_length=128)
    def __str__(self):
        return f'{self.topping}'
class Pizza(models.Model):
    pizza_type = models.ForeignKey(PizzaType, on_delete=models.CASCADE, related_name='pizza_types')
    size = models.ForeignKey(Size, on_delete=models.CASCADE,related_name='pizza_sizes')
    toppings = models.ManyToManyField(Topping, blank=True, related_name='topings')
    price = models.IntegerField()
    on_the_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_pizzas')
    def __str__(self):
        return f'{self.size} {self.pizza_type} pizza with {self.toppings} topings for ${self.price} dollars'
'''
sub related models
'''
class SubType(models.Model):
        sub_type = models.CharField(max_length=128)
        def __str__(self):
            return self.sub_type
class Sub(models.Model):
    sub_type = models.ForeignKey(SubType, on_delete=models.CASCADE, related_name='sub_types')
    size = models.ForeignKey(Size, on_delete=models.CASCADE,related_name='sub_sizes')
    price = models.IntegerField()
    listed = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_subs')
    def __str__(self):
        return f'{self.size} {self.sub_type} for {self.price}'
