from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, FormView
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy
from .forms import RegisterUser, UpdateProductForm
from .models import Users
from products.models import Products
from order.models import Basket
            
            
def RegisterUsers(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(request.POST['password1'])
            user.save()
            user = Users.objects.get(username=request.POST['username'])
            Basket.objects.create(
                owner_basket_id=user.pk
            )
            status = 'Вы успешно зарегистрированы, теперь необходимо войти в аккаунт'
        else:
            status = 'что то пошло не так :('

    else:
        form = RegisterUser()
        status = ''
    
    return render(request, 'users/register.html', {'form': form, 'status': status})
    
    
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    
class Profile(View):
    def get(self, request):
        try:
            user_pk = self.request.user.pk
            user = Users.objects.get(pk=user_pk)
            user_products = Products.objects.filter(owner_user=user_pk)
            context = {
                'user': user,
                'user_products': user_products,
                'status': ''
            }
        except:
            context = {
                'user': '',
                'user_products': '',
                'status': 'необходимо зарегистрироватся на сайте'
            }
        
        return render(request, 'users/profile.html', context)
    
    def post(self, request):
        user_pk = self.request.user.pk
        user = Users.objects.get(pk=user_pk)
        user_products = Products.objects.filter(owner_user=user_pk)
        button = request.POST['button']
        if button == 'add_product':
            user_status = str(user.user_status)
            if user_status == 'seller' or user_status == 'moder':
                return redirect('add_product')
            else:
                pass
        else:
            Products.objects.get(pk=button).delete()
        
        return render(request, 'users/profile.html', {'user': user, 'user_products': user_products})