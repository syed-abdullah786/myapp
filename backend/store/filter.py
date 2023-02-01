from django_filters.rest_framework import FilterSet
from .models import Order


class OrderFilter(FilterSet):
    class Meta:
        model = Order
        fields = {
            'created_at': ['gte', 'lte'],
            'status': ['exact'],
            'id':['exact']
        }