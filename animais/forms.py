from django import forms
from . import models


class AdicinarAnuncio(forms.ModelForm):

    class Meta:
        model = models.Animal
        fields = ['img_animal', 'titulo', 'nome_animal',
                  'idade', 'raca', 'animal', 'sexo', 'observacao',]


class AnimalDeleteForm(forms.ModelForm):
    class Meta:
        model = models.Animal
        fields = ['img_animal', 'titulo',  'nome_animal',
                  'idade', 'raca', 'animal', 'observacao']
