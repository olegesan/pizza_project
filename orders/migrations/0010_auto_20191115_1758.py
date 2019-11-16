# Generated by Django 2.2.7 on 2019-11-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20191115_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='kind',
            name='toppings_allowed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='toppings',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cart',
            field=models.ManyToManyField(blank=True, related_name='users_cart', to='orders.Cart'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='users_order', to='orders.Order'),
        ),
    ]
