import django_filters
from .models import Timing, Event


class TimeFilter(django_filters.FilterSet):
    class Meta:
        model = Timing
        fields = ["timing","date"]
