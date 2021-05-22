from django.contrib import admin
from .models import User,Manufacturer,Distributor,Retailer,Government_Body,Normal_User

# Register your models here.
admin.site.register(User)
admin.site.register(Manufacturer)
admin.site.register(Distributor)
admin.site.register(Retailer)
admin.site.register(Government_Body)
admin.site.register(Normal_User)