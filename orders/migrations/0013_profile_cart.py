# Generated by Django 2.2.7 on 2019-11-16 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20191115_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Cart'),
        ),
    ]
