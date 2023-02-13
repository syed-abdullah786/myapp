from django.urls import path

from . import views
from rest_framework_nested import routers

from .models import Customer

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet, basename="customers"),
router.register('products', views.ProductViewSet, basename="products"),
router.register('suppliers', views.SupplierViewSet, basename="suppliers"),
router.register('order', views.OrderView, basename="order"),
orders_router = routers.NestedDefaultRouter(router, 'order', lookup='order')
orders_router.register('notes', views.NoteViewSet, basename='order-notes')

urlpatterns = [
                  path('users/', views.User.as_view()),
                  path('export/csv/', views.export_csv, name='export_csv'),

                  # path('employees/', views.User.as_view()),
              ] + router.urls + orders_router.urls
