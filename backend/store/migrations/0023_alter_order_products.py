# Generated by Django 4.1.2 on 2023-02-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_alter_order_products_alter_product_price_gross_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='store.product'),
        ),
    ]