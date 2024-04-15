from django import forms

# Register your models here.
class EmployeeInfoForm(forms.Form):
    name=forms.CharField()
    salary=forms.IntegerField()
