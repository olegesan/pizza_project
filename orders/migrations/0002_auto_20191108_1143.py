# Generated by Django 2.2.7 on 2019-11-08 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.FloatField(),
        ),
    ]
