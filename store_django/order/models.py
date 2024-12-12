from django.db import models
from users.models import Users
from products.models import Products
from django.urls import reverse


class Basket(models.Model):
    owner_basket = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE
    )
    basket_sum = models.IntegerField(
        default=0
    )
    product_quantity = models.IntegerField(
        default=0
    )
    
    
class Product_in_basket(models.Model):
    where_product = models.ForeignKey(
        to=Basket,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to=Products,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return str(self.where_product)
    
    
class Refunds(models.Model):
    whose_refund = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE
    )
    refund = models.CharField(max_length=200)
    date_create = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('order:refund', kwargs={'refund_id': self.pk})
    
    def __str__(self):
        return self.whose_refund.username
    
    
class ApplicationOnRefund(models.Model):
    whose_application = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    accept = models.BooleanField(
        null=True,
        blank=True,
        default=''
    )
    date_create = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('order:application', kwargs={'application_id': self.pk})
    
    def __str__(self):
        return self.whose_application.username