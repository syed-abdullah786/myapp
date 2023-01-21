from django.urls import path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register( 'orders', views.OrdersViewSet , basename="orders")
urlpatterns = [
    path('orders/', views.OrdersView.as_view()),
    path('customers/', views.User.as_view()),
]
# urlpatterns = router.urls