from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView
from django.views import View
from .models import Basket, Product_in_basket
from products.models import Products
from .forms import BuyBasket
from django.urls import reverse, reverse_lazy


class UserBasket(View):
    def get(self, request):
        user_pk = self.request.user.pk
        basket = Basket.objects.get(owner_basket=user_pk)
        products_in_basket = Product_in_basket.objects.filter(where_product=basket.pk)
        
        return render(request, 'order/basket.html', {'basket': basket, 'products_in_basket': products_in_basket})
    
    def post(self, request):
        user_pk = self.request.user.pk
        basket = Basket.objects.get(owner_basket=user_pk)
        products_in_basket = Product_in_basket.objects.filter(where_product=basket.pk)
        button = request.POST['button']
        basket = Basket.objects.get(owner_basket=user_pk)
        product_in_basket = Product_in_basket.objects.get(pk=button)
        basket.basket_sum -= product_in_basket.product.price
        basket.product_quantity -= 1
        product = Products.objects.get(pk=product_in_basket.product.pk)
        product.quantity += 1
        product.save()
        basket.save()
        product_in_basket.delete()
        
        return render(request, 'order/basket.html', {'basket': basket, 'products_in_basket': products_in_basket})
    
    
class BuyBasket(FormView):
    form_class = BuyBasket
    template_name = 'order/buy_basket.html'
    success_url = reverse_lazy('home')
    
    def post(self, request, *args, **kwargs):
        user_basket = Basket.objects.get(owner_basket=self.request.user.pk)
        if user_basket.product_quantity == 0 and user_basket.basket_sum == 0:
            pass
        else:
            #логика отправки данных и покупки
            user_basket.basket_sum = 0
            user_basket.product_quantity = 0
            user_basket.save()
            Product_in_basket.objects.filter(where_product=user_basket.pk).delete()
        return super().post(request, *args, **kwargs)