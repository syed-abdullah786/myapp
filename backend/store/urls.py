from django.urls import path

from . import views
from rest_framework_nested import routers
from django.conf.urls.static import static
from django.conf import settings

from .models import Customer

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet, basename="customers"),
router.register('products', views.ProductViewSet, basename="products"),
router.register('editorder', views.EditOrderSerializerViewSet, basename="editorder"),
router.register('supplierproduct', views.SupplierProductViewSet, basename="supplierproduct"),
router.register('supplier', views.SupplierViewSet, basename="supplier"),
router.register('order', views.OrderView, basename="order"),
orders_router = routers.NestedDefaultRouter(router, 'order', lookup='order')
orders_router.register('notes', views.NoteViewSet, basename='order-notes'),
orders_router.register('files', views.FileViewSet, basename='files')

urlpatterns = [
                  path('users/', views.User.as_view()),
                  path('export/csv/', views.export_csv, name='export_csv'),
path('download/<int:id>/', views.FileDownloadView.as_view(), name='file_download'),

                  # path('employees/', views.User.as_view()),
              ] + router.urls + orders_router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
