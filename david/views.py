#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
#    return HttpResponse("Heloo dave")
    return render(request,'home.html')

def about(request):
#    return HttpResponse("aboit page")
    return render(request,'about.html')
