# Generated by Django 4.0 on 2021-12-19 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mainapp', '0008_order_customer_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='mainapp.cart', verbose_name='Корзина'),
        ),
    ]
