# Generated by Django 2.2.7 on 2019-11-09 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191108_1812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['menu_priority']},
        ),
        migrations.AlterModelOptions(
            name='kind',
            options={'ordering': ['-menu_priority']},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'ordering': ['-size']},
        ),
        migrations.AddField(
            model_name='category',
            name='menu_priority',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='kind',
            name='menu_priority',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='menu_priority',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='orders.Category'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
