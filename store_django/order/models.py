from django.db import models
from users.models import Users
from products.models import Products


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