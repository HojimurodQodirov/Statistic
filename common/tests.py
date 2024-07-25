from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Position, Country, City, Region, Neighborhood, Employee, Test
<<<<<<< Updated upstream
from .serializers import EmployeeSerializer, TestSerializer

=======
from .serializers import EmployeeSerializer


>>>>>>> Stashed changes
class PositionModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(title='Manager', slug='manager')

    def test_position_creation(self):
        self.assertEqual(self.position.title, 'Manager')
        self.assertEqual(str(self.position), 'Manager')


class EmployeeModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(title='Developer', slug='developer')
        self.country = Country.objects.create(title='Country A', slug='country-a')
        self.city = City.objects.create(title='City A', slug='city-a', country=self.country)
        self.region = Region.objects.create(title='Region A', slug='region-a', city=self.city)
        self.neighborhood = Neighborhood.objects.create(title='Neighborhood A', slug='neighborhood-a', region=self.region)
        self.employee = Employee.objects.create(
            full_name='John Doe',
            position=self.position,
            country=self.country,
            city=self.city,
            region=self.region,
            neighborhood=self.neighborhood
        )

    def test_employee_creation(self):
        self.assertEqual(self.employee.full_name, 'John Doe')
        self.assertEqual(str(self.employee), 'John Doe')


class TestModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(title='Developer', slug='developer')
        self.country = Country.objects.create(title='Country A', slug='country-a')
        self.city = City.objects.create(title='City A', slug='city-a', country=self.country)
        self.region = Region.objects.create(title='Region A', slug='region-a', city=self.city)
        self.neighborhood = Neighborhood.objects.create(title='Neighborhood A', slug='neighborhood-a', region=self.region)
        self.employee = Employee.objects.create(
            full_name='John Doe',
            position=self.position,
            country=self.country,
            city=self.city,
            region=self.region,
            neighborhood=self.neighborhood
        )
        self.test = Test.objects.create(
            title='Test 1',
            question='What is Django?',
            answer='A web framework',
            employee=self.employee,
            balls=90
        )

    def test_test_creation(self):
        self.assertEqual(self.test.title, 'Test 1')
        self.assertEqual(str(self.test), 'Test 1')


class EmployeeListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.position = Position.objects.create(title='Developer', slug='developer')
        self.country = Country.objects.create(title='Country A', slug='country-a')
        self.city = City.objects.create(title='City A', slug='city-a', country=self.country)
        self.region = Region.objects.create(title='Region A', slug='region-a', city=self.city)
        self.neighborhood = Neighborhood.objects.create(title='Neighborhood A', slug='neighborhood-a', region=self.region)
        self.employee = Employee.objects.create(
            full_name='John Doe',
            position=self.position,
            country=self.country,
            city=self.city,
            region=self.region,
            neighborhood=self.neighborhood
        )
        self.url = reverse('employee-list')

    def test_get_all_employees(self):
        response = self.client.get(self.url)
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class EmployeeListProcentViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.position = Position.objects.create(title='Developer', slug='developer')
        self.country = Country.objects.create(title='Country A', slug='country-a')
        self.city = City.objects.create(title='City A', slug='city-a', country=self.country)
        self.region = Region.objects.create(title='Region A', slug='region-a', city=self.city)
        self.neighborhood = Neighborhood.objects.create(title='Neighborhood A', slug='neighborhood-a', region=self.region)
        self.employee = Employee.objects.create(
            full_name='John Doe',
            position=self.position,
            country=self.country,
            city=self.city,
            region=self.region,
            neighborhood=self.neighborhood
        )
        self.test = Test.objects.create(
            title='Test 1',
            question='What is Django?',
            answer='A web framework',
            employee=self.employee,
            balls=90
        )
        self.url = reverse('employees-procent')

    def test_get_employee_percentage(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('procent', response.data)
