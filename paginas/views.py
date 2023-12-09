from django.shortcuts import render
from animais import models


def home(request):
    animais_destaques = models.Animal.objects.filter(destaque=True)
    return render(request,'home.html',{'animais_destaques':animais_destaques})

def base(request):
    return render(request,'base.html',)

# Create your views here.
