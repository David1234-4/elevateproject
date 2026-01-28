from django.shortcuts import render

def homepage(request):
#    return HttpResponse("Heloo dave")
    return render(request,'home.html')

def courses(request):
#    return HttpResponse("aboit page")
    return render(request,'courses.html')

def profiles(request):
    return render(request,'profiles.html')
