from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main.as_view(), name='home'),
    path('product/', views.Product.as_view()),
    path('product/reviews/', views.ReviewsPage.as_view(), name='reviews'),
    path('product/reviews/add_review/', views.AddReview.as_view()),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
]