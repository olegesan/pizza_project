# Generated by Django 2.2.7 on 2019-11-08 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_size_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='kinds',
            field=models.ManyToManyField(related_name='cat_kinds', to='orders.Kind'),
        ),
        migrations.AddField(
            model_name='category',
            name='sizes',
            field=models.ManyToManyField(blank=True, null=True, related_name='cat_sizes', to='orders.Size'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='orders.Size'),
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
    ]
