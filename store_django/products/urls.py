from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main.as_view(), name='home'),
    path('product/', views.Product.as_view()),
    path('product/reviews/', views.ReviewsPage.as_view(), name='reviews'),
    path('product/reviews/add_review/', views.AddReview.as_view()),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
<<<<<<< HEAD
    path('update/<int:pk>/', views.UpdateProduct.as_view(), name='update')
=======
    path('categorys/', views.categorys),
    path('users/profile/update/<int:pk>/', views.UpdateProduct.as_view())
>>>>>>> 29fdf43b36165b945ad51d0b485ad2370d31a970
]