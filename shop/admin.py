from django.contrib import admin
from . import models


admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.ProductSize)
admin.site.register(models.Image)
admin.site.register(models.Sizes)
admin.site.register(models.Order)
admin.site.register(models.OrderItem)