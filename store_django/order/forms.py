from django import forms
from .models import Basket, Product_in_basket


class BuyBasket(forms.Form):
    kard_number = forms.CharField(
        max_length=16,
        label='Номер карточки:'
    )
    pincode = forms.CharField(
        max_length=4,
        label='Пинкод:'
    )
    telephone_number = forms.CharField(
        max_length=16,
        label='Номер телефона:'
    )