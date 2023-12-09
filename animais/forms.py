from django import forms
from . import models


class AdicinarAnuncio(forms.ModelForm):
    
    class Meta:
        model = models.Animal
        fields = ['img_animal','nome','idade','raca','animal','sexo','observacao',]
        
class AnimalDeleteForm(forms.ModelForm):
    class Meta:
        model = models.Animal
        fields = ['img_animal', 'nome', 'idade', 'raca', 'animal','observacao']