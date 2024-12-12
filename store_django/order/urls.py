from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('basket/', views.UserBasket.as_view(), name='basket'),
    path('basket/buy/', views.BuyBasket.as_view(), name='buy'),
    path('refunds/', views.RefundsUser.as_view(), name='refunds_user'),
    path('refunds/refund/<int:refund_id>', views.Refund.as_view(), name='refund'),
    path('create_application/', views.CreateApplicationOnRefund.as_view(), name='create_application'),
    path('applications/', views.AplicationsOnRefundView.as_view(), name='applications'),
    path('applications_for_moder/', views.ApplicationsOnRefundForModer.as_view(), name='applications_for_moder'),
    path('refund_accept/', views.RefundAccept.as_view(), name='refund_accept'),
    path('basket/addication_balance/', views.AddicationBalance.as_view(), name='addication_balance')
]