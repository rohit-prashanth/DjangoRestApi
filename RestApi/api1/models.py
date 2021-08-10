from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
    emp_roll = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=20)
    emp_age = models.IntegerField()
    emp_location = models.CharField(max_length=20)

