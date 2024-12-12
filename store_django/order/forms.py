from django import forms
from .models import ApplicationOnRefund


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
    
    
class ApplicationOnRefundForm(forms.ModelForm):
    class Meta:
        model = ApplicationOnRefund
        fields = ['content', ]
        
        
class RefundAcceptForm(forms.Form):
    money = forms.CharField(
        max_length=20,
        label='деньги потраченые пользователем'
    )
    id = forms.IntegerField(label='id продукта')
    quantity = forms.IntegerField(label='Количество возвращаемого товара одного типа')
    
    
class AddicationBalanceForm(forms.Form):
    money = forms.IntegerField(label='Количество денег которое вы хотите положить себе на баланс')