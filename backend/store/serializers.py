from django.contrib.auth.models import User
from django.db import transaction
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from .models import Order, Customer, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Customer
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    products = ProductSerializer(many=True)
    class Meta:
        model = Order
        fields = '__all__'
    def save(self, **kwargs):
        request = self.context['request']
        if request.method == 'POST':
            with transaction.atomic():
                print('self.validated_data',self.validated_data)
                customer = Customer(sur_name=self.validated_data['customer']['sur_name'],
                         last_name=self.validated_data['customer']['last_name'],
                         company_name=self.validated_data['customer']['company_name'],
                         address=self.validated_data['customer']['address'],
                         zip_code=self.validated_data['customer']['zip_code'],
                         country=self.validated_data['customer']['country'],
                         phone=self.validated_data['customer']['phone'],
                         mail=self.validated_data['customer']['mail'],
                         vat_number=self.validated_data['customer']['vat_number'],
                         )
                customer.save()

                order_items = [
                    Product(title=item['title'], price_net=item['price_net'], price_gross=item['price_gross'],quantity=item['quantity'],sku=item['sku']) for item
                    in self.validated_data['products']]
                Product.objects.bulk_create(order_items)
                for product in order_items:
                    product_id = product.id
                    print(product_id)
                print('order_items',order_items)

                order = Order(shipping = self.validated_data['shipping'],
                              order_tax_type = self.validated_data['order_tax_type'],
                              payment = self.validated_data['payment'],
                              status = self.validated_data['status'],
                              priority = self.validated_data['priority'],
                              shipping_status = self.validated_data['shipping_status'],
                              assigned_to = self.validated_data['assigned_to'],
                              customer = customer,
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
                print('self.validated_data',self.validated_data)

                # for customer update
                obj.customer.sur_name=self.validated_data['customer']['sur_name']
                obj.customer.last_name=self.validated_data['customer']['last_name']
                obj.customer.company_name=self.validated_data['customer']['company_name']
                obj.customer.address=self.validated_data['customer']['address']
                obj.customer.zip_code=self.validated_data['customer']['zip_code']
                obj.customer.country=self.validated_data['customer']['country']
                obj.customer.phone=self.validated_data['customer']['phone']
                obj.customer.mail=self.validated_data['customer']['mail']
                obj.customer.vat_number=self.validated_data['customer']['vat_number']
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
                obj.shipping_status = self.validated_data['shipping_status']
                obj.assigned_to = self.validated_data['assigned_to']
                obj.save()
                print(obj)

