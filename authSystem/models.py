from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.first_name + ' ' + self.last_name
