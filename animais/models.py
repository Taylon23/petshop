from django.db import models
from . import choices
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils import timezone
import os


class RacaAnimal(models.Model):
    raca = models.CharField(max_length=50, verbose_name='raça')
    
    def __str__(self):
        return self.raca
    
class TipoAnimal(models.Model):
    tipo_animal = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipo_animal
    
    def save(self, *args, **kwargs):
        # Garantir que a primeira letra da categoria seja maiúscula
        self.tipo_animal= self.tipo_animal.capitalize()
        super(TipoAnimal, self).save(*args, **kwargs)
    
class Animal(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    img_animal = models.ImageField(upload_to='img_animal/', verbose_name='imagem do animal')
    titulo = models.CharField(max_length=200)
    nome_animal = models.CharField(max_length=50, default='Sem nome')
    raca = models.ForeignKey(RacaAnimal, verbose_name='raça',default='SRD (Sem Raça Definida)', on_delete=models.PROTECT)
    animal = models.ForeignKey(TipoAnimal, verbose_name='Animal', on_delete=models.PROTECT)
    sexo = models.CharField(max_length=1, choices=choices.SEXO_ANIMAL_CHOICES, verbose_name='sexo')
    data_criacao = models.DateField(auto_now_add=True)
    observacao = models.TextField(default='sem observações')
    destaque = models.BooleanField(default=False)
    favoritado = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Nome: {self.nome_animal} - Raça: {self.raca} - Sexo: {self.sexo} - Data criação: {self.data_criacao}'


@receiver(pre_delete, sender=Animal)
def delete_animal_image(sender, instance, **kwargs):
    # Verifica se a instância do livro tem uma imagem associada a ela
    if instance.img_animal:
        # Exclui o arquivo de imagem quando o livro é excluído
        if os.path.isfile(instance.img_animal.path):
            os.remove(instance.img_animal.path)
