from wsgiref.util import FileWrapper

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
import csv
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .filter import OrderFilter
import mimetypes
from django.http import FileResponse
from .models import Order, Customer, Product, Supplier, Note, SupplierProduct, File
from .serializers import OrderSerializer, CustomerSerializer, ProductSerializer, UserSerializer, EditProductSerializer, \
    SupplierSerializer, NoteSerializer, SupplierProductSerializer, EditOrderSerializer, FileSerializer


class FileDownloadView(APIView):
    def get(self, request, id, format=None):
        queryset = File.objects.get(id=id)
        file_handle = queryset.specs.path
        document = open(file_handle, 'rb')
        response = HttpResponse(FileWrapper(document), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % queryset.specs.name
        return response
    # def get(self, request):
    #     file = open('./uploads/specs/Winning_1.pdf_2.pdf', 'rb')
    #     response = FileResponse(file)
    #     return response


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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = OrderFilter
    ordering_fields = ['id']
    search_fields = ['customer__sur_name', 'customer__last_name', 'products__title']
    filterset_fields = ['id', 'status']
    permission_classes = [IsAuthenticated]


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class EditOrderSerializerViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = EditOrderSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierProductViewSet(ModelViewSet):
    queryset = SupplierProduct.objects.all()
    serializer_class = SupplierProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['prod_id'] = self.request.data.get('prod_id')
        return context


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = EditProductSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['order_id'] = self.request.data.get('order_id')
        return context


class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer

    def get_queryset(self):
        order = self.kwargs['order_pk']
        return Note.objects.filter(order_id=order)


class FileViewSet(ModelViewSet):
    serializer_class = FileSerializer

    def get_queryset(self):
        order = self.kwargs['order_pk']
        return File.objects.filter(order_id=order)


    # @action(methods=['GET'], detail=True)
    # def download(self, request, **kwargs):
    #     att = self.get_object()
    #     file_handle = att.file.open()
    #     mimetype, _ = mimetypes.guess_type(att.file.path)
    #     response = FileResponse(file_handle, content_type=mimetype)
    #     response['Content-Length'] = att.file.size
    #     response['Content-Disposition'] = "attachment; filename={}".format(att.filename)
    #     return response


class User(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="yourfile.csv"'

    writer = csv.writer(response)
    writer.writerow(
        ['K_Companyname', 'K_First Name', 'K_Last Name', 'K_Street', 'K_Street 2', 'K_ZIP', 'K_City', 'K_Country',
         'K_Tel', 'K_E-Mail', 'VAT',
         'L_Company Name', 'L_First Name', 'L_Last Name', 'L_Street', 'L_Street 2', 'L_ZIP', 'L_City', 'L_Country',
         'Order Date', 'Order Payment', 'Order Shipping', 'Status',
         'SKU', 'QTY', 'Article Name', 'Net Price', 'Tax', 'Price Gross', 'Netto Gesamt', 'Amount', 'Discount((%)'
         ])

    models = Order.objects.all()
    for model in models:
        for prod in model.products.all():
            writer.writerow(

                [model.customer.company_name, model.customer.sur_name, model.customer.last_name, model.customer.street,
                 model.customer.street_2, model.customer.zip_code, model.customer.city, model.customer.country,
                 model.customer.phone, model.customer.mail,
                 model.customer.vat_number, model.customer.l_company_name, model.customer.l_sur_name,
                 model.customer.l_last_name, model.customer.l_street,
                 model.customer.l_street_2, model.customer.l_zip_code, model.customer.l_city, model.customer.l_country,
                 model.created_at, model.payment, model.shipping, model.shipping_status,
                 prod.sku, prod.quantity, prod.title, prod.price_net, model.order_tax_type, prod.price_gross,
                 prod.price_net, prod.price_gross, prod.discount])
    return response
