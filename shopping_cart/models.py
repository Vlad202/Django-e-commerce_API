from django.db import models
from django.contrib.auth.models import User
from shop.models import OrderItem


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_item =  models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()