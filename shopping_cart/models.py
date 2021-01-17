from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_item =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    def __str__(self):
        return '{} - {} - {}'.format(self.user.username, self.order_item.name, self.quantity)