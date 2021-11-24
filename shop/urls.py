from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import *
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('user', UserViewSet)
# router.register('sign_up/', RegistrationViewSet)
router.register('product', ProductViewSet)
router.register('cart', CartViewSet)

urlpatterns = [
                  path('', include(router.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
