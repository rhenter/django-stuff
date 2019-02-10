from django_filters import Filter
from django_filters.fields import Lookup


class ListFilter(Filter):
    def filter(self, qs, value):
        values = value.split(',')
        return super().filter(qs, Lookup(values, 'in'))
