from django.shortcuts import render
from animais import models


def home(request):
    animais_destaques = models.Animal.objects.filter(destaque=True)
    tipo_cachorro = models.TipoAnimal.objects.get(tipo_animal='Cachorro')
    tipo_gato = models.TipoAnimal.objects.get(tipo_animal='Gato')
    tipo_outros_animais = models.TipoAnimal.objects.get(
        tipo_animal='Outro animal')
    cachorros = models.Animal.objects.filter(animal=tipo_cachorro)
    gatos = models.Animal.objects.filter(animal=tipo_gato)
    outros_animais = models.Animal.objects.filter(animal=tipo_outros_animais)
    return render(request, 'home.html', {'animais_destaques': animais_destaques, 
                                         'cachorros': cachorros, 
                                         'gatos': gatos, 'outros_animais': outros_animais})


def base(request):
    return render(request, 'base.html',)