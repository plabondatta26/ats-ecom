from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (JSONParser, FormParser, MultiPartParser)


class CartViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated, ]
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(user=self.request.user.id).order_by('-id')
