# Generated by Django 2.2.7 on 2019-11-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_category_menu_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='kind',
            name='menu_priority',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_priority',
            field=models.IntegerField(null=True),
        ),
    ]
