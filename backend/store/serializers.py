from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Order, Customer, Product, Supplier, Note, SupplierProduct, File


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class GetSupplierProductSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()

    class Meta:
        model = SupplierProduct
        fields = '__all__'


class SupplierProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierProduct
        fields = '__all__'

    def save(self, **kwargs):
        request = self.context['request']
        if request.method == 'POST':
            print('self.validated_data', self.validated_data)
            prod_id = self.context['prod_id']
            supp = SupplierProduct.objects.create(**self.validated_data)
            product = Product.objects.get(id=prod_id)
            product.supplier.add(supp)
            self.instance = supp
        if request.method == 'PUT':
            product = self.instance
            for attr, value in self.validated_data.items():
                setattr(product, attr, value)
            product.save()
            self.instance = product
        return self.instance


class ProductSerializer(serializers.ModelSerializer):
    supplier = GetSupplierProductSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class EditProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('supplier',)

    def save(self, **kwargs):
        request = self.context['request']
        if request.method == 'POST':
            order_id = self.context['order_id']
            product = Product.objects.create(**self.validated_data)
            order = Order.objects.get(id=order_id)
            order.products.add(product)
            self.instance = product
        if request.method == 'PUT':
            product = self.instance
            for attr, value in self.validated_data.items():
                setattr(product, attr, value)
            product.save()
            self.instance = product
        return self.instance


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class EditOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('products','created_at','customer' )

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def save(self, **kwargs):
        request = self.context['request']
        print('validated data', self.validated_data)
        if request.method == 'POST':
            with transaction.atomic():
                company_name = self.validated_data['customer'].get('company_name', '')
                street_2 = self.validated_data['customer'].get('street_2', '')
                vat_number = self.validated_data['customer'].get('vat_number', '')
                l_company_name = self.validated_data['customer'].get('l_company_name', '')
                l_street_2 = self.validated_data['customer'].get('l_street_2', '')
                customer = Customer(sur_name=self.validated_data['customer']['sur_name'],
                                    last_name=self.validated_data['customer']['last_name'],
                                    company_name=company_name,
                                    street=self.validated_data['customer']['street'],
                                    street_2=street_2,
                                    zip_code=self.validated_data['customer']['zip_code'],
                                    city=self.validated_data['customer']['city'],
                                    country=self.validated_data['customer']['country'],
                                    phone=self.validated_data['customer']['phone'],
                                    mail=self.validated_data['customer']['mail'],
                                    vat_number=vat_number,
                                    l_sur_name=self.validated_data['customer']['l_sur_name'],
                                    l_last_name=self.validated_data['customer']['l_last_name'],
                                    l_company_name=l_company_name,
                                    l_street=self.validated_data['customer']['l_street'],
                                    l_street_2=l_street_2,
                                    l_zip_code=self.validated_data['customer']['l_zip_code'],
                                    l_city=self.validated_data['customer']['l_city'],
                                    l_country=self.validated_data['customer']['l_country'],
                                    )
                customer.save()

                # code for pythonanywhere, it didnot support bulk_create
                order_items = []
                for item in self.validated_data['products']:
                    prod = Product(title=item['title'], price_net=item['price_net'], price_gross=item['price_gross'],
                                   quantity=item['quantity'], discount=item['discount'], sku=item['sku'])
                    prod.save()
                    order_items.append(prod)

                # order_items = [
                #     Product(title=item['title'], price_net=item['price_net'], price_gross=item['price_gross'],
                #             quantity=item['quantity'], discount=item['discount'], sku=item['sku']) for item
                #     in self.validated_data['products']]
                # Product.objects.bulk_create(order_items)
                for product in order_items:
                    product_id = product.id
                    print(product_id)
                print('order_items', order_items)

                order = Order(shipping=self.validated_data['shipping'],
                              order_tax_type=self.validated_data['order_tax_type'],
                              payment=self.validated_data['payment'],
                              status=self.validated_data['status'],
                              priority=self.validated_data['priority'],
                              assigned_to=self.validated_data['assigned_to'],
                              customer=customer,
                              )
                order.save()
                order.products.set(order_items)

                # for item in self.validated_data['products']:
                #     # title = product['title']
                #     Product(title=item.title, price_net=item.price_net, price_gross=item.price_gross, quantity=item.quantity,
                #             sku=item.sku)
                #     Product.save()


        elif request.method == 'PATCH':
            with transaction.atomic():
                obj = Order.objects.get(id=self.instance.id)
                print('self.validated_data', self.validated_data)

                # for customer update
                obj.customer.sur_name = self.validated_data['customer']['sur_name']
                obj.customer.last_name = self.validated_data['customer']['last_name']
                if self.validated_data['customer']['company_name']:
                    obj.customer.company_name = self.validated_data['customer']['company_name']
                obj.customer.street = self.validated_data['customer']['street']
                if self.validated_data['customer']['street_2']:
                    obj.customer.street_2 = self.validated_data['customer']['street_2']
                obj.customer.zip_code = self.validated_data['customer']['zip_code']
                obj.customer.country = self.validated_data['customer']['country']
                obj.customer.city = self.validated_data['customer']['city']
                obj.customer.phone = self.validated_data['customer']['phone']
                obj.customer.mail = self.validated_data['customer']['mail']
                if self.validated_data['customer']['vat_number']:
                    obj.customer.vat_number = self.validated_data['customer']['vat_number']
                obj.customer.l_sur_name = self.validated_data['customer']['l_sur_name']
                obj.customer.l_last_name = self.validated_data['customer']['l_last_name']
                if self.validated_data['customer']['l_company_name']:
                    obj.customer.l_company_name = self.validated_data['customer']['l_company_name']
                obj.customer.l_street = self.validated_data['customer']['l_street']
                if self.validated_data['customer']['l_street_2']:
                    obj.customer.l_street_2 = self.validated_data['customer']['l_street_2']
                obj.customer.l_zip_code = self.validated_data['customer']['l_zip_code']
                obj.customer.l_country = self.validated_data['customer']['l_country']
                obj.customer.l_city = self.validated_data['customer']['l_city']
                obj.customer.save()

                # for products update and create new
                products = []
                for item in self.validated_data['products']:
                    product, created = Product.objects.get_or_create(**item)
                    products.append(product)
                obj.products.set(products)
                print('good')
                # for order update
                obj.shipping = self.validated_data['shipping']
                obj.order_tax_type = self.validated_data['order_tax_type']
                obj.payment = self.validated_data['payment']
                obj.status = self.validated_data['status']
                obj.priority = self.validated_data['priority']
                obj.assigned_to = self.validated_data['assigned_to']
                obj.save()
                print(obj)
