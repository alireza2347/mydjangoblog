from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    #return HttpResponse('hi world!')
    return render(request , 'about.html')

def home(request):
    #return HttpResponse('Home')
    return render(request , 'Home.html')
