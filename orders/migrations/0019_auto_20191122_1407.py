# Generated by Django 2.2.7 on 2019-11-22 19:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0018_auto_20191120_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ManyToManyField(related_name='user_order', to=settings.AUTH_USER_MODEL),
        ),
    ]
