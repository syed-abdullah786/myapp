from django.urls import path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register( 'customers', views.Customer , basename="customers"),
# router.register( 'products', views.Product , basename="products"),
# router.register( 'order_item', views.Order_Item , basename="order_item"),
router.register( 'order', views.OrderView , basename="order"),


urlpatterns = [
    path('users/', views.User.as_view())
    # path('employees/', views.User.as_view()),
]+ router.urls