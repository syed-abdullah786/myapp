# Generated by Django 4.1.2 on 2023-02-01 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_customers_customer_rename_orders_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now_add=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_status',
            field=models.CharField(default='pending', max_length=30),
        ),
    ]
