from django_filters import rest_framework as filters

from .models import Apartment


class ApartmentFilter(filters.FilterSet):

    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    min_room = filters.NumberFilter(field_name="rooms", lookup_expr="gte")
    min_baths = filters.NumberFilter(field_name="bathrooms", lookup_expr="gte")

    class Meta:
        model = Apartment
        fields = '__all__'