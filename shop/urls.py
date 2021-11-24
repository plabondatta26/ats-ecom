from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *
router = routers.DefaultRouter()
router.register('user', UserViewSet)
# router.register('sign_up/', RegistrationViewSet)
router.register('product', ProductViewSet)
router.register('cart', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
