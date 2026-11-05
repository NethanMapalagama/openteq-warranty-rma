from django.contrib import admin
from .models import Customer, Product, Vendor, WarrantyCase, DamagePhoto

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(WarrantyCase)
admin.site.register(DamagePhoto)
