from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('basket/', views.UserBasket.as_view(), name='basket'),
    path('basket/buy/', views.BuyBasket.as_view(), name='buy'),
]