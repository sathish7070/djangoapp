from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def tellmetime(request):
    time=datetime.datetime.now()
    result=('<h1> HI THE TIME IS '+str(time)+'</h1>')
    return HttpResponse(result)
