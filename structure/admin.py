from django.contrib import admin
from .models import World_version, Customer_Account, Country, Clan


# Register your models here.
admin.site.register(World_version)
admin.site.register(Customer_Account)
admin.site.register(Country)
admin.site.register(Clan)