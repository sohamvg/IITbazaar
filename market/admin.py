from django.contrib import admin
from market.models import Category,Seller,Product

# Register your models here.

admin.site.register(Category)
admin.site.register(Seller)
admin.site.register(Product)