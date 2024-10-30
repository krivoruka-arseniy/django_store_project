from django.contrib import admin
from .models import Basket, Product_in_basket

admin.site.register(Basket)
admin.site.register(Product_in_basket)