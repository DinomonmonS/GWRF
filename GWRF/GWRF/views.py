from django.shortcuts import render
from .models import teacher

def index(request):
    teach = teacher.objects.all()
    return render(request,"GWRF/index.html",{'content':teach})