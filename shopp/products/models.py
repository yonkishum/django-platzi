from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Product(models.Model):
    """docstring for Product."""
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name