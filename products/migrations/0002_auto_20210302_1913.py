# Generated by Django 3.1.7 on 2021-03-02 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product_stock', to='products.product'),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField()),
                ('transaction_type', models.IntegerField(choices=[(0, 'OUTPUT'), (1, 'INPUT')])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_transactions', to='products.product')),
            ],
        ),
    ]
