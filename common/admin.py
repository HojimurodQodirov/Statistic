from django.contrib import admin
from .models import Test, Position, Employee, Region, Neighborhood, Country, City, Question, Answer

admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Region)
admin.site.register(Neighborhood)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Answer)