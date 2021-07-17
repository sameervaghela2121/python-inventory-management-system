from django.contrib import admin
from . models import Inventory,Register,Bill

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Register)
admin.site.register(Bill)