import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='country__title', lookup_expr='iexact')
    city = django_filters.CharFilter(field_name='city__title', lookup_expr="iexact")
    region = django_filters.CharFilter(field_name='region__title', lookup_expr='iexact')
    neighborhood = django_filters.CharFilter(field_name='neighborhood__title', lookup_expr='iexact')


    class Meta:
        model = Employee
        fields = ['country', 'city', 'region', 'neighborhood']
