from django.contrib.auth.models import User
from django.db import models

from .validators import validate_file


class Supplier(models.Model):
    allegro_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    iban = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    street = models.CharField(max_length=70)
    zip_code = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    bank_detail = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)


class SupplierProduct(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    sku = models.IntegerField()
    buying_price = models.IntegerField()


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=250)
    price_net = models.DecimalField(max_digits=8, decimal_places=2)
    price_gross = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.IntegerField()
    sku = models.IntegerField()
    supplier = models.ManyToManyField(SupplierProduct, related_name='products', null=True)


class Customer(models.Model):
    sur_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    company_name = models.CharField(max_length=50, null=True, default=None)
    street = models.CharField(max_length=150)
    street_2 = models.CharField(max_length=150, null=True, default=None)
    zip_code = models.CharField(max_length=50)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    mail = models.EmailField()
    vat_number = models.CharField(max_length=30, null=True, default=None)
    l_sur_name = models.CharField(max_length=40)
    l_last_name = models.CharField(max_length=40)
    l_company_name = models.CharField(max_length=50, null=True, default=None)
    l_street = models.CharField(max_length=150)
    l_street_2 = models.CharField(max_length=150, null=True, default=None)
    l_zip_code = models.CharField(max_length=50)
    l_city = models.CharField(max_length=150)
    l_country = models.CharField(max_length=150)


class Order(models.Model):
    SHIPPING_METHOD = [
        ('standard', 'standard'),
        ('international', 'international'),
        ('express', 'express')
    ]
    ORDER_TAX_TYPE = [
        ('19%', '19%'),
        ('IGL', 'IGL'),
        ('Drittland', 'Drittland')
    ]
    PAYMENT = [
        ('??berweisung', '??berweisung'),
        ('PayPal', 'PayPal'),
        ('eBay Managed Payments', 'eBay Managed Payments')
    ]
    ORDER_STATUS = [
        ('lead', 'lead'),
        ('new-order', 'new-order'),
        ('sourcing', 'Sourcing'),
        ('prepare-shipment', 'prepare-shipment'),
        ('pickup', 'pickup'),
        ('done', 'done'),
        ('return', 'return')
    ]
    shipping = models.CharField(max_length=20, choices=SHIPPING_METHOD)
    order_tax_type = models.CharField(max_length=20, choices=ORDER_TAX_TYPE)
    payment = models.CharField(max_length=40, choices=PAYMENT)
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=40, choices=ORDER_STATUS)
    priority = models.CharField(max_length=20, default='normal')
    assigned_to = models.ForeignKey(User, on_delete=models.RESTRICT)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    products = models.ManyToManyField(Product,null=True)


class Note(models.Model):
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)


class File(models.Model):
    specs = models.FileField(upload_to='specs', null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
