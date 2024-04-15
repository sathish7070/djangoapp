from django.shortcuts import render
import datetime

# Create your views here.
#def display(request):
 #   return render(request,'demoapps/abc.html')

#def display(request):
 #   date=datetime.datetime.now()
  #  date_dict={'display_date' : date}
   # return render (request,'demoapps/abc.html',context=date_dict)

def display(request):

    message='hi'
    date=datetime.datetime.now()
    hour=int(date.strftime('%H'))
    if hour < 12 :
        message+= ' GOOD MORNING'

    else:
        message += ' GOOD EVENING'

    name='sathish'        
    date_dict={'display_date' : date,'empname':name,'greetings': message}
    return render (request,'demoapps/abc.html',context=date_dict)
