from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Orders, Customers, Products, Order_Item


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields = '__all__'

class Order_ItemSerializers(serializers.ModelSerializer):
    product_id = ProductSerializers(read_only=True)
    class Meta:
        model= Order_Item
        fields = '__all__'


class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model= Customers
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class OrderSerializers(serializers.ModelSerializer):
    customer_id = CustomerSerializers(read_only=True)
    products = Order_ItemSerializers(read_only=True,many=True)
    assigned_to = UserSerializer(read_only=True)
    class Meta:
        model = Orders
        # fields = ['id','customer_id','products']
        fields = '__all__'

