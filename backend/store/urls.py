from django.urls import path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register( 'neworders', views.OrderViewSet , basename="neworders")
urlpatterns = [
    path('orders/', views.OrdersView.as_view()),
    path('customers/', views.User.as_view()),
]+ router.urls