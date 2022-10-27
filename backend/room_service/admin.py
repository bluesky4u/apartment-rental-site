from typing import Sequence
from django.contrib import admin
from .models import ApartmentContact, ApartmentImage, ApartmentType, Location, Apartment, ApartmentFeature


class ImageInline(admin.TabularInline):
    model = ApartmentImage

    
@admin.register(ApartmentFeature)
class FeaturesAdmin(admin.ModelAdmin):
    search_fields: Sequence[str] = ('name',)


@admin.register(ApartmentType)
class TypeAdmin(admin.ModelAdmin):
    search_fields: Sequence[str] = ('name',)
    

@admin.register(Apartment)    
class ApartmentAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    readonly_fields = ('date_added',)
    list_display = ('name', 'price', 'rooms', 'apartment_type')
    list_filter = ('apartment_type', 'rooms')
    search_fields: Sequence[str] = ('name', 'apartment_type__name')
    autocomplete_fields: Sequence[str] = ('features', 'apartment_type')
    search_help_text = "Enter name or apartment type to search"
    show_full_result_count: bool = True

    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('region', 'city', 'address')
    list_filter = ('region', 'city',)
    search_fields: Sequence[str] = ('region', 'city',)


@admin.register(ApartmentContact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone')


@admin.register(ApartmentImage)
class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.site_header = "Rent A Home Admin"
