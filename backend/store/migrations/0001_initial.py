# Generated by Django 4.1.2 on 2023-02-22 09:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sur_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('company_name', models.CharField(default=None, max_length=50, null=True)),
                ('street', models.CharField(max_length=150)),
                ('street_2', models.CharField(default=None, max_length=150, null=True)),
                ('zip_code', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=150)),
                ('country', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('vat_number', models.CharField(default=None, max_length=30, null=True)),
                ('l_sur_name', models.CharField(max_length=40)),
                ('l_last_name', models.CharField(max_length=40)),
                ('l_company_name', models.CharField(default=None, max_length=50, null=True)),
                ('l_street', models.CharField(max_length=150)),
                ('l_street_2', models.CharField(default=None, max_length=150, null=True)),
                ('l_zip_code', models.CharField(max_length=50)),
                ('l_city', models.CharField(max_length=150)),
                ('l_country', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allegro_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('iban', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=70)),
                ('street', models.CharField(max_length=70)),
                ('zip_code', models.CharField(max_length=70)),
                ('city', models.CharField(max_length=70)),
                ('country', models.CharField(max_length=70)),
                ('bank_detail', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.IntegerField()),
                ('buying_price', models.IntegerField()),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('price_net', models.DecimalField(decimal_places=2, max_digits=8)),
                ('price_gross', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('sku', models.IntegerField()),
                ('supplier', models.ManyToManyField(null=True, related_name='products', to='store.supplierproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping', models.CharField(choices=[('standard', 'standard'), ('international', 'international'), ('express', 'express')], max_length=20)),
                ('order_tax_type', models.CharField(choices=[('19%', '19%'), ('IGL', 'IGL'), ('Drittland', 'Drittland')], max_length=20)),
                ('payment', models.CharField(choices=[('??berweisung', '??berweisung'), ('PayPal', 'PayPal'), ('eBay Managed Payments', 'eBay Managed Payments')], max_length=40)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('lead', 'lead'), ('new-order', 'new-order'), ('sourcing', 'Sourcing'), ('prepare-shipment', 'prepare-shipment'), ('pickup', 'pickup'), ('done', 'done'), ('return', 'return')], max_length=40)),
                ('priority', models.CharField(default='normal', max_length=20)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.customer')),
                ('products', models.ManyToManyField(null=True, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specs', models.FileField(null=True, upload_to='specs')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
            ],
        ),
    ]
