from rest_framework import serializers
from .models import EmployeeDetails
class EmployeeDetailsSerializer(serializers.Serializer):
    emp_roll = serializers.CharField(max_length=20)
    emp_name = serializers.CharField(max_length=20)
    emp_age = serializers.IntegerField()
    emp_location = serializers.CharField(max_length=20)


