from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Product(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    prod_name = models.CharField(max_length=200)
    prod_desc = models.CharField(max_length=200)
    prod_price = models.IntegerField()
    prod_image = models.CharField(max_length=500,default="https://cdn.vectorstock.com/i/1000x1000/93/30/new-product-coming-soon-poster-vector-29899330.webp")

    def __str__(self):
        return self.prod_name
    
    def get_absolute_url(self):
        return reverse('mobileApp:detail',kwargs={'pk':self.pk})
    
