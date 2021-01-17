from django.db import models
from authSystem.models import Person
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=32)
    category_name = models.CharField(max_length=32, default='')
    has_dimensions = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    CURRENCIES = (
        ('$', 'USD'),
        ('₴', 'UAH'),
        ('₽', 'RUB'),
    )
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=244)
    care = models.TextField()
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE, default=None)
    has_discount = models.BooleanField(default=False)
    cost = models.FloatField(default=0.0)
    discount_cost = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='USD')
    def save(self, *args, **kwargs):
        self.cost = round(self.cost, 2)
        super(Product, self).save(*args, **kwargs)
    def __str__(self):
        return self.name


class Sizes(models.Model):
    size = models.CharField(max_length=8)
    def __str__(self):
        return self.size


class ProductSize(models.Model):
    product = models.ForeignKey(Product, related_name='product_size', on_delete=models.CASCADE)
    size = models.ForeignKey(Sizes, related_name='product_size', on_delete=models.CASCADE)
    def __str__(self):
        return self.size.size

class Image(models.Model):
    product = models.ForeignKey(Product, related_name='image', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.product.name

class Order(models.Model):
    # user = models.ForeignKey(Person, related_name='person', on_delete=models.CASCADE, default=None)
    order_id = models.CharField(max_length=48)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    father_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=12, blank=True, help_text='Contact phone number')
    email = models.CharField(max_length=64)
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    region = models.CharField(max_length=32)
    address = models.CharField(max_length=144)
    post_index = models.IntegerField()
    description = models.CharField(max_length=244)
    cost = models.FloatField()
    # closed = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        self.cost = round(self.cost, 2)
        super(Order, self).save(*args, **kwargs)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, blank=True, related_name='order_item', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='product_order', on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, related_name='product_order_size', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
    cost = models.FloatField()
    def save(self, *args, **kwargs):
        self.cost = round(self.cost, 2)
        super(OrderItem, self).save(*args, **kwargs)
    def __str__(self):
        return 'ID - %s %s : %s' % (self.order.pk, self.product.name, self.size)