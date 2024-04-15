from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def one(request):
    return HttpResponse('<h1> THE NUM IS ONE </h1>')

def two(request):
    return HttpResponse('<h1> THE NUM IS TWO </h1>')

def three(request):
    return HttpResponse('<h1> THE NUM IS THREE </h1>')
