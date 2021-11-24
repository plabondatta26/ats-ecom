from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ProductModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    image = models.FileField(blank=False, upload_to='Product/images')
    price = models.CharField(max_length=100, blank=False, null=False)
    stock = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class CartModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.user.username + ' ' + str(self.quantity)
