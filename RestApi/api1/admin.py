from django.contrib import admin
from .models import EmployeeDetails
# Register your models here.
@admin.register(EmployeeDetails)
class AdminEmployeeDetails(admin.ModelAdmin):
    list_display = ['emp_roll','emp_name','emp_age','emp_location']