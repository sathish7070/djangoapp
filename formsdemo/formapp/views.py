from django.shortcuts import render
from . import forms

# Create your views here.
def empdetailsview(request):
    form=forms.EmployeeInfoForm()
    empinfo={'form':form}
    return render (request,'formapp/input.html',context=empinfo)