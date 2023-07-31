from django.db import models

# Create your models here.

class Product_data(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=1000)