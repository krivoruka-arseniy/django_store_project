from django.contrib import admin
from .models import Basket, Product_in_basket, Refunds, ApplicationOnRefund

admin.site.register(Basket)
admin.site.register(Product_in_basket)
admin.site.register(Refunds)
admin.site.register(ApplicationOnRefund)