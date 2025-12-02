from .models import Property
from django_filters import FilterSet


class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'city':['exact'],
            'property_type':['exact'],
            'price_per_night':['gt','lt'],
        }