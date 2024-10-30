from django.db import models
from django.contrib.auth.models import AbstractUser


class Status(models.Model):
    status_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.status_name


class Users(AbstractUser):
    user_status = models.ForeignKey(
        to=Status,
        on_delete=models.CASCADE,
        default=1
    )
    
    def __str__(self):
        return self.username