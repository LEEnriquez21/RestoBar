from django.contrib import admin
from .models import Product, Table, Reservation
# Register your models here.
admin.site.register(Product)
admin.site.register(Table)
admin.site.register(Reservation)
