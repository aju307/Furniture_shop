from django.db import models

# Create your models here.
class Registration(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=100,null=True , blank=True)
    Username = models.CharField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True, blank=True)
class CartDB(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    ProductName = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)
class savecheckout(models.Model):
    Product_name = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    totalPrice = models.IntegerField(null=True, blank=True)

