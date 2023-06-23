from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categories(models.Model):
    title=models.CharField(max_length=50)
    slug=models.SlugField(unique=True,max_length=50)
    
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.title

class Products (models.Model):    
    user=models.ForeignKey(User,related_name='products', on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    price=models.IntegerField()
    description=models.TextField()
    slug=models.SlugField(unique=True,max_length=50)
    image=models.ImageField(upload_to='product_image/',default='product_default.png', height_field=None, width_field=None, max_length=None)
    category=models.ForeignKey(Categories,related_name='products', verbose_name=("category"), on_delete=models.CASCADE)
    created_on=models.DateField(auto_now_add=True)
    last_updated=models.DateField(auto_now=True)

    class Meta:
        verbose_name = ("products")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.title

