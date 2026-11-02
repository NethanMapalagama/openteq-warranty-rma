from django.db import models

# Create your models here.

# Customer
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


# Product
class Product(models.Model):
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=200)
    serial_number = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return f"{self.brand} {self.model_name}"