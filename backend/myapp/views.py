from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
# from .models import Products
# from .serializers import ProductSerializers


# class ProductViewSet(ModelViewSet):
#     # queryset = Products.objects.all()
#     # serializer_class = ProductSerializers
#     # permission_classes = [IsAuthenticated]
#     # def get_permissions(self):
#     #     if self.request.method == 'GET':
#     #         return [AllowAny()]
#     #     return [IsAuthenticated()]