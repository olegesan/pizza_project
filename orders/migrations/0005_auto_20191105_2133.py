# Generated by Django 2.2.7 on 2019-11-06 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191105_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_type', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='listed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pizza',
            name='listed',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='menu_pizzas', to='orders.Menu'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('listed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_subs', to='orders.Menu')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_sizes', to='orders.Size')),
                ('sub_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_types', to='orders.SubType')),
            ],
        ),
    ]