from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .filter import OrderFilter
from .models import Order, Customer, Product
from .serializers import OrderSerializer, CustomerSerializer, ProductSerializer, UserSerializer


class OrderView(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    # def get_queryset(self):
    #     queryset = Order.objects.all()
    #     if not self.request.user.is_staff:
    #         print('stokes', self.request.user.id)
    #         queryset = Order.objects.filter(assigned_to=self.request.user.id)
    #
    #     return queryset

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = OrderFilter
    search_fields = ['customer__sur_name', 'customer__last_name', 'products__title']
    filterset_fields = ['id', 'status']
    permission_classes = [IsAuthenticated]




# class Customer(ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#
#
# class Product(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
class User(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class OrderViewSet(ModelViewSet):
#     def get_queryset(self):
#         queryset = Order.objects.all()
#         if not self.request.user.is_staff:
#             print('stokes', self.request.user.id)
#             queryset = Order.objects.filter(assigned_to=self.request.user.id)
#
#         return queryset
#
#     serializer_class = OrderSerializer
#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_class = OrderFilter
#     search_fields = ['customer_id__sur_name', 'customer_id__last_name', 'products__product_id__title']
#     filterset_fields = ['id', 'status']
#     permission_classes = [IsAuthenticated]
