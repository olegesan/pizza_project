# Generated by Django 2.2.7 on 2019-11-06 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_type', models.CharField(max_length=128)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_prices', to='orders.Price')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_sizes', to='orders.Size')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_type', models.CharField(max_length=128)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='piza_prices', to='orders.Price')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_sizes', to='orders.Size')),
                ('toppings', models.ManyToManyField(blank=True, related_name='topings', to='orders.Topping')),
            ],
        ),
    ]
