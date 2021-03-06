# Generated by Django 3.1.7 on 2021-03-03 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210303_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product_transactions', to='products.product'),
        ),
    ]
