from django_filters import rest_framework as filters

from .models import Apartment


class ApartmentFilter(filters.FilterSet):

    class Meta:
        model = Apartment
        fields = '__all__'