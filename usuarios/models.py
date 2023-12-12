from django.db import models
from django.contrib.auth.models import User
from animais import models as models_animal


class Favorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    animal = models.ForeignKey(models_animal.Animal, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Usuario: {self.usuario} - Anuncio: {self.animal.titulo}'