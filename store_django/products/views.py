from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView, CreateView, UpdateView
from .models import Products, Reviews, Category
from order.models import Basket, Product_in_basket
from users.models import Users, Status
from django.views import View
from .forms import AddReview, AddProduct
from django.urls import reverse, reverse_lazy


def categorys(request):
    data = Category.objects.all()
    
    return render(request, 'products/categorys.html', {'data': data})


class Main(View):
    def get(self, request):
        products = Products.objects.filter(public=True)
        
        return render(request, 'products/main.html', {'products': products})
    
    def post(self, request):
        products = Products.objects.filter(public=True)
        button = request.POST['button']
        
        if button == 'filter':
            product_category = request.POST['product_cat']
            if product_category == 'all':
                pass
            else:
                products = Products.objects.filter(product_cat=product_category, public=True)
        else:
            request.session['product_pk'] = button
            return redirect('product/')
        
        return render(request, 'products/main.html', {'products': products})
    
    
class Product(View):
    def get(self, request):
        product_pk = request.session['product_pk']
        product = Products.objects.get(pk=product_pk)
        status = ''
        
        return render(request, 'products/product.html', {'product': product, 'status': status})
    
    def post(self, request):
        product_pk = request.session['product_pk']
        product = Products.objects.get(pk=product_pk)
        button = request.POST['button']
        
        if button == 'hide':
            try:
                user_pk = self.request.user.pk
                user_uniform = Users.objects.get(pk=user_pk)
                user_status = str(user_uniform.user_status)
                if user_status == 'moder':
                    product.public = False
                    product.save()
                    status = 'продукт успешно скрыт'
                else:
                    status = 'функция только для модераторов'
            except:
                status = 'необходимо зарегистрироватся на сайте'
        else:
            if product.quantity > 0:
                try:
                    user = self.request.user
                    user_basket = Basket.objects.get(owner_basket=user)
                    Product_in_basket.objects.create(
                        where_product_id=user_basket.pk,
                        product_id=product_pk
                    )
                
                    product.quantity -= 1
                    product.save()
                    user_basket.basket_sum += product.price
                    user_basket.product_quantity += 1
                    user_basket.save()
                    status = 'Продукт успешно добавлен в корзину!'
                except:
                    status = 'необходимо зарегистрироватся на сайте'
            else:
                status = 'Данный продукт уже закончился :('
                    
        
        return render(request, 'products/product.html', {'product': product, 'status': status})
    
    
class ReviewsPage(View):
    def get(self, request):
        product_pk = request.session['product_pk']
        reviews = Reviews.objects.filter(where_review=product_pk)
        
        return render(request, 'products/reviews.html', {'reviews': reviews})
    
    def post(self, request):
        product_pk = request.session['product_pk']
        reviews = Reviews.objects.filter(where_review=product_pk)
        user = self.request.user
        review_pk = request.POST['button']
        review = Reviews.objects.get(pk=review_pk)
        if review.owner_review_id == user.pk:
            review.delete()
        else:
            pass
        
        return render(request, 'products/reviews.html', {'reviews': reviews})
    
    
class AddReview(FormView):
    form_class = AddReview
    template_name = 'products/add_review.html'
    success_url = reverse_lazy('reviews')
    
    def post(self, request, *args, **kwargs):
        try:
            product_pk = request.session['product_pk']
            Reviews.objects.create(
                where_review_id=product_pk,
                owner_review_id=self.request.user.pk,
                review_name=request.POST['review_name'],
                review_content=request.POST['review_content']
            )
        except:
            pass
        return super().post(request, *args, **kwargs)
    
    
class AddProduct(CreateView):
    form_class = AddProduct
    template_name = 'products/add_product.html'
    success_url=reverse_lazy('home')
    
    def form_valid(self, form):
        w = form.save(commit=False)
        w.owner_user_id = self.request.user.pk
        return super().form_valid(form)
    
    
class UpdateProduct(UpdateView):
    model = Products
    fields = (
        'product_name',
        'product_description',
        'price',
        'quantity',
        'product_cat',
        'product_img',
        'public'
    )
    template_name = 'products/update_product.html'
    success_url = reverse_lazy('home')