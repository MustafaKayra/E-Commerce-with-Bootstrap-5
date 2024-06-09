<<<<<<< HEAD
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=1000,unique=True)

    def __str__(self):
        return f"{self.name}"    

class Product(models.Model):
    name = models.CharField(max_length=1000,blank=False,null=False)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="C:/Users/kayra/ecommercial/static/img")
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs): #Slug alanını otomatik olarak kişinin ismine göre kaydetmesi
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

class Report(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    email = models.CharField(max_length=100,null=False,blank=False)
    report = models.TextField()

    def __str__(self):
        return f"{self.report}"
=======
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=1000,unique=True)

class Product(models.Model):
    name = models.CharField(max_length=1000,blank=False,null=False)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="C:/Users/kayra/ecommercial/static/img")
>>>>>>> 814535c (Add files via upload)
