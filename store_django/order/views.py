from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView
from django.views import View
from .models import Basket, Product_in_basket, Refunds, ApplicationOnRefund
from products.models import Products
from .forms import BuyBasket, ApplicationOnRefundForm, RefundAcceptForm, AddicationBalanceForm
from django.urls import reverse_lazy
from users.models import Users


class AddicationBalance(FormView):
    template_name = 'order/addication_balance.html'
    form_class = AddicationBalanceForm
    success_url = reverse_lazy('order:basket')
    
    def form_valid(self, form):
        user = Users.objects.get(pk=self.request.user.pk)
        user.money_balance += int(self.request.POST['money'])
        user.save()
        
        return super().form_valid(form)


class UserBasket(View):
    def get(self, request):
        user_pk = self.request.user.pk
        user = Users.objects.get(pk=user_pk)
        basket = Basket.objects.get(owner_basket=user_pk)
        products_in_basket = Product_in_basket.objects.filter(where_product=basket.pk)
        
        return render(request, 'order/basket.html', {'basket': basket, 'products_in_basket': products_in_basket, 'user': user})
    
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
        user_pk = self.request.user.pk
        user_basket = Basket.objects.get(owner_basket=user_pk)
        if user_basket.product_quantity == 0 and user_basket.basket_sum == 0:
            pass
        else:
            #логика отправки данных и покупки
            products = Product_in_basket.objects.filter(where_product=user_basket.pk)
            all_product = []
            for i in products:
                all_product.append(i.product.pk)
                all_product.append(i.product.product_name)
                all_product.append(i.product.price,)
            Refunds.objects.create(
                whose_refund_id=self.request.user.pk,
                refund=all_product
            )
            user = Users.objects.get(pk=user_pk)
            print(user.money_balance, user_basket.basket_sum)
            new_balance = user.money_balance - user_basket.basket_sum
            print(new_balance)
            if new_balance <= 0:
                pass
            else:
                user.money_balance = new_balance
                user.save()
                products.delete()
                user_basket.basket_sum = 0
                user_basket.product_quantity = 0
                user_basket.save()
            
        return super().post(request, *args, **kwargs)
    
    
class RefundsUser(View):
    def get(self, request):
        pk_application = request.session['pk_application']
        user_pk = ApplicationOnRefund.objects.get(pk=pk_application).whose_application.pk
        refunds = Refunds.objects.filter(whose_refund=user_pk)
        
        return render(request, 'order/refunds_list.html', {'refunds': refunds})

    def post(self, request):
        pk_application = request.session['pk_application']
        user_pk = ApplicationOnRefund.objects.get(pk=pk_application).whose_application.pk
        refunds = Refunds.objects.filter(whose_refund=user_pk)
        
        return render(request, 'order/refunds_list.html', {'refunds': refunds})
    
    
class Refund(View):
    def get(self, request, **kwargs):
        refund = Refunds.objects.get(pk=kwargs['refund_id'])
        
        return render(request, 'order/refund.html', {'refund': refund})

    def post(self, request, **kwargs):
        button = request.POST['button']
        pk_application = request.session['pk_application']
        application = ApplicationOnRefund.objects.get(pk=pk_application)
        if button == 'accept':
            request.session['refund_user_pk'] = application.whose_application.pk
            return redirect('order:refund_accept')
        else:
            application.accept = False
            application.save()
        
        return redirect('order:applications')
    
    
class RefundAccept(FormView):
    template_name = 'order/refund_accept.html'
    form_class = RefundAcceptForm
    success_url = reverse_lazy('order:applications_for_moder')
    
    def form_valid(self, form):
        user_pk = self.request.session['refund_user_pk']
        money = self.request.POST['money']
        user = Users.objects.get(pk=user_pk)
        user.money_balance += int(money)
        user.save()
        pk_application = self.request.session['pk_application']
        application = ApplicationOnRefund.objects.get(pk=pk_application)
        application.accept = True
        application.save()
        pk_product = self.request.POST['id']
        product = Products.objects.get(pk=pk_product)
        product.quantity += int(self.request.POST['quantity'])
        product.save()
        
        return super().form_valid(form)
    
    
class CreateApplicationOnRefund(CreateView):
    form_class = ApplicationOnRefundForm
    template_name = 'order/create_application.html'
    success_url = reverse_lazy('order:applications')

    def form_valid(self, form):
        valid_f = form.save(commit=False)
        valid_f.whose_application_id = self.request.user.pk
        return super().form_valid(form)
    
    
class ApplicationsOnRefundForModer(View):
    def get(self, request):
        applications = ApplicationOnRefund.objects.filter(whose_application=self.request.user.pk, accept='')
        
        return render(request, 'order/applications_for_moder.html', {'applications': applications})

    def post(self, request):
        request.session['pk_application'] = request.POST['pk_application']
        
        return redirect('order:refunds_user')
           
    
class AplicationsOnRefundView(View):
    def get(self, request):
        applications = ApplicationOnRefund.objects.filter(whose_application=self.request.user.pk)
        
        return render(request, 'order/applications.html', {'applications': applications})
    
    def post(self, request):
        applications = ApplicationOnRefund.objects.filter(whose_application=self.request.user.pk)
        button = request.POST['button']
        ApplicationOnRefund.objects.get(pk=button).delete()
        
        return render(request, 'order/applications.html', {'applications': applications})