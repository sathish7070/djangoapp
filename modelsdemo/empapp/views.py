from django.shortcuts import render
#from django.http import HttpResponse
from empapp.models import Employee
# Create your views here.
def empdetails(request):
    #return httpresponse('<h1>edhu firstu pannathu eppadi views la </h1>')
    name='sathish'
    emp_data=Employee.objects.all()
    emp_dict={'emp_list':emp_data}

    return render (request,'empapp/employee.html',context=emp_dict)
