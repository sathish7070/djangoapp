from django.shortcuts import render,redirect,HttpResponse
from crudapp.models import Student
from crudapp.forms import StudentForm

# Create your views here.
def retrieve_view(request):
    Student=Student.objects.all()
    return render(request,'crudapp/index.html',{'Student':Student})

def create_view(request):
    form=StudentForm()
    if request.method=='POST':
       form=StudentForm(request.POST)
       if form.is_valid():
           form.save() 
           return redirect('/check')
    return render(request,'crudapp/create.html',{'form':form})

def delete_view(request,id):
    Student=Student.objects.get(id=id)
    Student.delete()
    return redirect('/check')

def update_view(request,id):
    

    Student =Student.objects.get (id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=Student)
        if form.is_valid():
            form.save()
            return redirect('/check')
    return render(request, 'crudapp/update.html', {'form': form, 'Student': Student})


# Middleware auth
def userCheck(request):
    if 1 == 1:

        print("user check")
        # return HttpResponse("middleware")
        pass
    else:
        print("====Redirect to specific apage due to failed validations")




#def update_view(request,id):
    

 #   student_instance = get_object_or_404(student, id=id)

    #if request.method == 'POST':
       # form = StudentForm(request.POST, instance=student_instance)
        #if form.is_valid():
         #   form.save()
          #  return redirect('/check')
    #else:
     #   form = StudentForm(instance=student_instance)

    #return render(request, 'crudapp/update.html', {'form': form, 'student': student_instance})
