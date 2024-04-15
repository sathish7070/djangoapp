from django.db import models

# Create your models here.
class Employee(models.Model):
    empno=models.IntegerField()
    empname=models.CharField(max_length=20)
    empsalary=models.IntegerField()
    empaddress=models.CharField(max_length=30)

def __str__(self):
    return 'Employee details an shared'+empname
    
