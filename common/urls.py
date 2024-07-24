from django.urls import path
from .views import PositionList, CountryList, CityList, RegionList, NeighborhoodList, EmployeeList, TestList, EmployeeListProcent

urlpatterns = [
    path('positions/', PositionList.as_view(), name='position-total-balls'),
    path('countries/', CountryList.as_view(), name='country-list'),
    path('cities/', CityList.as_view(), name='city-list'),
    path('regions/', RegionList.as_view(), name='region-list'),
    path('neighborhoods/', NeighborhoodList.as_view(), name='neighborhood-list'),
    path('employees_procent/', EmployeeListProcent.as_view(), name='employees-procent'),
    path('employees/', EmployeeList.as_view(), name='employee-list'),
    path('tests/', TestList.as_view(), name='test-list'),
]
