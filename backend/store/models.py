from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=30)
    price_net = models.IntegerField()
    price_gross = models.IntegerField()
    quantity = models.IntegerField()
    sku = models.IntegerField()


class Customers(models.Model):
    sur_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    zip_code=models.CharField(max_length=50,null=True,default='RET62536',blank=True)
    country = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    mail = models.EmailField()
    vat_number=models.IntegerField()

class Orders(models.Model):
    SHIPPING_METHOD = [
        ('standard', 'standard'),
        ('international', 'international'),
        ('express', 'express')
    ]
    ORDER_TAX_TYPE =[
        ('19%', '19%'),
        ('IGL', 'IGL'),
        ('Drittland', 'Drittland')
    ]
    PAYMENT = [
        ('Überweisung', 'Überweisung'),
        ('PayPal', 'PayPal'),
        ('eBay Managed Payments', 'eBay Managed Payments')
    ]
    ORDER_STATUS = [
        ('new', 'new'),
        ('WIP', 'WIP'),
        ('shipped', 'shipped'),
        ('return', 'return')
    ]
    shipping = models.CharField(max_length=20,choices=SHIPPING_METHOD)
    order_tax_type = models.CharField(max_length=20,choices=ORDER_TAX_TYPE)
    payment = models.CharField(max_length=40,choices=PAYMENT)
    created_at = models.DateField(max_length=20)
    status = models.CharField(max_length=40,choices=ORDER_STATUS)
    priority = models.CharField(max_length=20,default='normal')
    shipping_status= models.CharField(max_length=30,default='Pending')
    assigned_to = models.ForeignKey(User,on_delete=models.RESTRICT)
    customer_id = models.ForeignKey(Customers, on_delete=models.RESTRICT,related_name='customer')

class Order_Item(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.RESTRICT,related_name='products')
    product_id = models.ForeignKey(Products, on_delete=models.RESTRICT)


