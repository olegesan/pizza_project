# Generated by Django 2.2.7 on 2019-11-24 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_auto_20191124_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstatus',
            name='status_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='statuses_cat', to='orders.StatusCatergory'),
        ),
    ]