# Generated by Django 2.2.7 on 2019-11-08 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20191108_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='size',
            name='price',
        ),
    ]
