from django.db import models
from django.contrib.auth.models import User

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


# Vendor
class Vendor(models.Model):
    name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


# WarrantyCase
class WarrantyCase(models.Model):
    # Own keys
    case_reference = models.CharField(max_length=20,unique=True)
    status = models.CharField(max_length=50)
    damage_description = models.TextField()
    damage_location = models.TextField()
    accessories_received = models.TextField(blank=True, null=True)
    date_logged = models.DateField(auto_now_add=True)
    date_dispatched = models.DateField(blank=True, null=True)
    date_returned = models.DateField(blank=True, null=True)
    deadline_date = models.DateField(blank=True, null=True)
    repair_notes = models.TextField(blank=True, null=True)
    customer_notified = models.BooleanField(default=False)

    # Foreign keys
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, blank=True, null=True)
    logged_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.case_reference


# DamagePhoto
class DamagePhoto(models.Model):
    photo = models.ImageField(upload_to='damage_photos/')
    case = models.ForeignKey(WarrantyCase, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for {self.case.case_reference}"