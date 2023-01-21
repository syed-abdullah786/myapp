from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Orders, Customers, Products, Order_Item
from .serializers import OrderSerializers, CustomerSerializers, ProductSerializers, Order_ItemSerializers, \
    UserSerializer


class OrdersView(generics.ListAPIView):

    def get_queryset(self):
        queryset = Orders.objects.all()
        if not self.request.user.is_staff:
            print('stokes',self.request.user.id)
            queryset = Orders.objects.filter(assigned_to = self.request.user.id)

        return queryset

    serializer_class = OrderSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['customer_id__sur_name','customer_id__last_name','products__product_id__title']
    filterset_fields= ['id']
    permission_classes = [IsAuthenticated]

class Customers(generics.ListAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializers


class Products(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializers


class Order_Item(generics.ListAPIView):
    queryset = Order_Item.objects.all()
    serializer_class = Order_ItemSerializers

class User(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
