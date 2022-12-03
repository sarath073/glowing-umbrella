from django.shortcuts import render
from django.http import HttpResponse
from . models import anime
from . models import more_anime

# Create your views here.

def function_one(request):
    x=anime.objects.all()
    y=more_anime.objects.all()
    return render(request,"index.html",{'r':x,'s':y})



