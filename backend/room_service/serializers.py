from rest_framework import serializers

from .models import (Apartment, ApartmentContact, ApartmentFeature,
                     ApartmentImage, ApartmentType, Location)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class ApartmentFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentFeature
        fields = "__all__"

class ApartmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentType
        fields = "__all__"


class ApartmentSerializer(serializers.ModelSerializer):
    features = ApartmentFeatureSerializer(many=True, read_only=False)
    class Meta:
        model = Apartment
        fields = ["id", "rooms", "bedrooms", "kitchen", "garage",
                  "living_room", "furnishing", "price", "apartment_type", "location", "apartment_image", "name", "bathrooms", "description", "features", "apartment_contact" ]
        depth = 1


class ApartmentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentImage
        fields = "__all__"


class ApartmentContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentContact
        fields = '__all__'
