from . import models


def categorias_globais(request):
    animais = models.Animal.objects.all()
    tipo_animais = models.TipoAnimal.objects.all()
    return {'animais':animais,'tipos_animais':tipo_animais}