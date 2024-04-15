from django  import forms
from crudapp.models import Student

# Create your models here.
class StudentForm(forms.ModelForm):
    class Meta :
        model=Student
        fields= '__all__'


