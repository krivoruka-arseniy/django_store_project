from django import forms
from .models import Users
from products.models import Products
from django.contrib.auth.forms import UserCreationForm


class RegisterUser(UserCreationForm):
    class Meta:
        model = Users
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        
        
class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'product_name',
            'product_description',
            'price',
            'quantity',
            'product_cat',
            'product_img',
            'public'
        ]