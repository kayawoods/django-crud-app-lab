from django.shortcuts import render

from django.http import HttpResponse

def home(reqest): 
    return HttpResponse('<h1>Flower Museum ◟(๑• ᴗ •)◞❁</h1>')

def about(request):
     return render(request, 'about.html')