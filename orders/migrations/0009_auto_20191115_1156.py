# Generated by Django 2.2.7 on 2019-11-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20191115_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
