from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.RegisterUsers, name='register'),
    path('register/login/', views.LoginUser.as_view(), name='login'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('profile/update/<int:pk>/', views.UpdateProduct.as_view()),
]