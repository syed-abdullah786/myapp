from django_filters.rest_framework import FilterSet
from .models import Orders


class OrderFilter(FilterSet):
    class Meta:
        model = Orders
        fields = {
            'created_at': ['gt', 'lt'],
            'status': ['exact'],
            'id':['exact']
        }