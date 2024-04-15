from django.contrib import admin
from empapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    emp_details=['empno','empname','empsalary','empaddress']
admin.site.register(Employee,EmployeeAdmin)
