from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class ShippingAddress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    full_name = models.CharField(
        max_length=100,
    )
    city = models.CharField(
        max_length=150,
    )
    street = models.CharField(max_length=150)
    zip_code = models.IntegerField(blank=True, null=True)


class Order(models.Model):
    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)

    total_price = models.IntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    quantity = models.SmallIntegerField()
