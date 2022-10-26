from django import views
from django.shortcuts import render
from rest_framework import viewsets, filters

from .filters import ApartmentFilter

from .models import ApartmentContact, ApartmentFeature, ApartmentImage, Location, ApartmentType, Apartment
from .serializers import ApartmentContactSerializer, ApartmentFeatureSerializer, ApartmentImageSerializer, LocationSerializer, ApartmentSerializer, ApartmentTypeSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ApartmentTypeViewSet(viewsets.ModelViewSet):
    queryset = ApartmentType.objects.all()
    serializer_class = ApartmentTypeSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    filterset_class = ApartmentFilter
    search_fields = ['name', 'apartment_type__name', 'location__city', 'location__address', 'location__region']


class ApartmentImageViewSet(viewsets.ModelViewSet):
    queryset = ApartmentImage.objects.all()
    serializer_class = ApartmentImageSerializer



class ApartmentFeatureViewSet(viewsets.ModelViewSet):
    queryset = ApartmentFeature.objects.all()
    serializer_class = ApartmentFeatureSerializer


class ApartmentContactViewSet(viewsets.ModelViewSet):
    queryset = ApartmentContact.objects.all()
    serializer_class = ApartmentContactSerializer
