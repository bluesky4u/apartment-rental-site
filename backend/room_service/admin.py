from django.contrib import admin
from .models import ApartmentImage, ApartmentType, Location, Apartment, ApartmentFeature


admin.site.register(ApartmentType)
admin.site.register(Location)
admin.site.register(Apartment)
admin.site.register(ApartmentImage)
admin.site.register(ApartmentFeature)
