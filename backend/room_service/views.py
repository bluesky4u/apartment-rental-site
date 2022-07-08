from django import views
from django.shortcuts import render
from rest_framework import viewsets

from .models import ApartmentImage, Location, ApartmentType, Apartment
from .serializers import ApartmentImageSerializer, LocationSerializer, ApartmentSerializer, ApartmentTypeSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class ApartmentTypeViewSet(viewsets.ModelViewSet):
    queryset = ApartmentType.objects.all()
    serializer_class = ApartmentTypeSerializer


class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class ApartmentImageViewSet(viewsets.ModelViewSet):
    queryset = ApartmentImage.objects.all()
    serializer_class = ApartmentImageSerializer

