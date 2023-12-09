from django.db import models
from . import choices
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
    img_animal = models.ImageField(upload_to='img_animal/', verbose_name='imagem do animal')
    nome = models.CharField(max_length=50, default='Sem nome')
    raca = models.ForeignKey(RacaAnimal, verbose_name='raça',default='SRD (Sem Raça Definida)', on_delete=models.CASCADE)
    animal = models.ForeignKey(TipoAnimal, verbose_name='Animal', on_delete=models.CASCADE)
    sexo = models.CharField(max_length=1, choices=choices.SEXO_ANIMAL_CHOICES, verbose_name='sexo')
    idade = models.IntegerField()
    data_criacao = models.DateField(auto_now_add=True)
    destaque = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Nome: {self.nome} - Raça: {self.raca} - Sexo: {self.sexo} - Idade: {self.idade} - Data criação: {self.data_criacao}'


@receiver(pre_delete, sender=Animal)
def delete_animal_image(sender, instance, **kwargs):
    # Verifica se a instância do livro tem uma imagem associada a ela
    if instance.img_animal:
        # Exclui o arquivo de imagem quando o livro é excluído
        if os.path.isfile(instance.img_animal.path):
            os.remove(instance.img_animal.path)
