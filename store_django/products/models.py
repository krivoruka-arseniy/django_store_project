from django.db import models
from users.models import Users
from django.urls import reverse


class Category(models.Model):
    cat_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.cat_name
    
    
class Products(models.Model):
    owner_user = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE
    )
    product_img = models.ImageField(upload_to='product_imgs')
    product_name = models.CharField(max_length=30)
    product_description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    product_cat = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        db_index=True
    )
    public = models.BooleanField(
        default=True,
        db_index=True
    )
    product_create_time = models.DateTimeField(auto_now_add=True)
    
    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})

    def __str__(self):
        return self.product_name
    
    class Meta:
        ordering = ['-product_create_time']
        indexes = [
            models.Index(fields=['-product_create_time'])
        ]
    
    
class Reviews(models.Model):
    where_review = models.ForeignKey(
        to=Products,
        on_delete=models.CASCADE
    )
    owner_review = models.ForeignKey(
        to=Users,
        on_delete=models.CASCADE
    )
    review_name = models.CharField(max_length=15)
    review_content = models.CharField(max_length=50)
    review_create_time = models.DateTimeField(auto_now_add=True)