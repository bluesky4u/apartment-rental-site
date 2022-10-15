from django.db import models
from django.utils.timezone import now


class Location(models.Model):

    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=20)
    long = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)


class ApartmentType(models.Model):

    name = models.CharField(max_length=20, default="Unspecified")
    image = models.ImageField(upload_to="apartment_type", default="")


class Apartment(models.Model):

    name = models.CharField(max_length=200, default="")

    rooms = models.IntegerField(default=0)
    # bedrooms = models.IntegerField(default=0) deleting this because rooms just mean bedrooms
    bathrooms = models.IntegerField(default=0)

    kitchen = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    living_room = models.BooleanField(default=True)
    furnishing = models.BooleanField(default=False)

    price = models.DecimalField(decimal_places=2, max_digits=10)

    apartment_type = models.ForeignKey(
        to=ApartmentType, on_delete=models.CASCADE)
    location = models.ForeignKey(to=Location, on_delete=models.CASCADE)

    description = models.TextField(default="")
    features = models.ManyToManyField(to="ApartmentFeature", blank=True)

    apartment_contact = models.ForeignKey(to="ApartmentContact", on_delete=models.CASCADE)

    available_from = models.DateField(default=now, blank=True)
    available_to = models.DateField(default=now, blank=True)
    available_to_undefined = models.BooleanField(default=True)


class ApartmentImage(models.Model):
    
    apartment = models.ForeignKey(to=Apartment, on_delete=models.CASCADE, related_name="apartment_image")
    image = models.ImageField(upload_to="apartment_images")


class ApartmentFeature(models.Model):

    name = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class ApartmentContact(models.Model):

    email = models.EmailField()
    phone = models.CharField(max_length=20)
