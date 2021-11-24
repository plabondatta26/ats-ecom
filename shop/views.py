from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user=self.request.user.id).order_by('-id')
