from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=1000,unique=True)

class Product(models.Model):
    name = models.CharField(max_length=1000,blank=False,null=False)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="C:/Users/kayra/ecommercial/static/img")