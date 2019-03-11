from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

'''
class ProductManager(models.Manager):
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return super(ProductManager, self).filter(timestamp__lte=timezone.now())
'''
class Category(models.Model):
    name = models.CharField(max_length=50, help_text='Product category')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=60)
    phone = PhoneNumberField(null=False, blank=True, unique=True)
    address = models.TextField(max_length=500, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this product."""
        return reverse('market:seller-detail', args=[str(self.id)])


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=1000, help_text='brief description of the product', blank=True)
    image = models.ImageField(default='default.png',blank=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ManyToManyField(Category, help_text='Categories for this product', blank=True)
    #available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=1)
    # Manager
    #objects = ProductManager()


    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this product."""
        return reverse('market:product-detail', args=[str(self.id)])

