from django import forms
from .models import Reviews, Products


class AddReview(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = [
            'review_name',
            'review_content'
        ]
        
        
class AddProduct(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'product_img',
            'product_name',
            'product_description',
            'price',
            'quantity',
            'product_cat'
        ]