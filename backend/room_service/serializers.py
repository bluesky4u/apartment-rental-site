from dataclasses import fields
from rest_framework import serializers

from .models import ApartmentImage, Location, Apartment, ApartmentType


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        fields = "__all__"


class ApartmentSerializer(serializers.ModelSerializer):
    apartment_image = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="ApartmentImageViewSet", allow_null=True)

    class Meta:
        model = Apartment
        fields = ["id", "rooms", "bedrooms", "kitchen", "garage",
                  "living_room", "furnishing", "price", "apartment_type", "location", "apartment_image" ]
        depth = 1


class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = "__all__"
