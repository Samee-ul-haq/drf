from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def home(request):
    #return HttpResponse("Hello , Django World")
    tasks=Task.objects.all()
    return render(request,"index.html",{"tasks":tasks})

def contact(request):
    return HttpResponse("This is contact page")