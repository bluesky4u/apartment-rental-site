from django.db import models


class Location(models.Model):

    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=20)
    long = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)


class ApartmentType(models.Model):

    name = models.CharField(max_length=20, default="Unspecified")


class Apartment(models.Model):

    name = models.CharField(max_length=200, default="")

    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()

    kitchen = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    living_room = models.BooleanField(default=True)
    furnishing = models.BooleanField(default=False)

    price = models.DecimalField(decimal_places=2, max_digits=10)

    apartment_type = models.ForeignKey(
        to=ApartmentType, on_delete=models.CASCADE)
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)


class ApartmentImage(models.Model):
    
    apartment = models.ForeignKey(to=Apartment, on_delete=models.CASCADE, related_name="apartment_image")
    image = models.ImageField(upload_to="apartment_images")
    