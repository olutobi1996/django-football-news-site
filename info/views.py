from django.shortcuts import render
from .models import Info

def info(request):
    return render(request,"info.html")
    
