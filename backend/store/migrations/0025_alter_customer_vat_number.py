# Generated by Django 4.1.2 on 2023-02-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_alter_order_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='vat_number',
            field=models.CharField(max_length=30),
        ),
    ]