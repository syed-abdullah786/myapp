from django.urls import path

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register( 'products', views.ProductViewSet , basename="product")
# urlpatterns = [
#     # path('products/', views.ProductViewSet.as_view()),
# ]
urlpatterns = router.urls