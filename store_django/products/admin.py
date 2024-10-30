from django.contrib import admin
from .models import Category, Products, Reviews

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Reviews)