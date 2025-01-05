from django.shortcuts import render
from .models import info

def info(request):
    return render(request,"info.html")
    
