# Generated by Django 2.2.7 on 2019-11-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20191108_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ['-size']},
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.FloatField(blank=True),
        ),
    ]
