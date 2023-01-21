from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
# from .models import Products
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    class Meta(BaseUserCreateSerializer.Meta):

        fields = ['id','first_name','last_name','username','email','password']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserCreateSerializer.Meta):

        fields = ['id','is_staff','username','email']

# class ProductSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Products
#         fields = '__all__'
