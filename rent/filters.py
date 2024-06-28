import django_filters
from.models import houses

class HouseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    room_is_booked = django_filters.BooleanFilter()
    room_capacity = django_filters.NumberFilter()

    class Meta:
        model = houses
        fields = ('name', 'room_is_booked', 'room_capacity')