from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import BooleanField


# Create your models here.
class Register(AbstractUser):
    is_publisher = BooleanField(default=False)
    is_customer = BooleanField(default=False)


class Publisher(models.Model):
    user=models.ForeignKey('Register',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)


    def __str__(self):
        return f'{self.name} {self.email}'


class Customer(models.Model):
    user=models.ForeignKey('Register',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    address = models.TextField()





class blog(models.Model):
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    Information = models.TextField(null=True, blank=True)
    Image = models.FileField(upload_to='documents/')
