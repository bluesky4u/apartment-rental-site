from django.contrib import admin
from .models import ApartmentType, Location, Apartment


admin.site.register(ApartmentType)
admin.site.register(Location)
admin.site.register(Apartment)
