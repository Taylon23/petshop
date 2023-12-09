from django.contrib import admin
from . import models


admin.site.register(models.Animal)
admin.site.register(models.RacaAnimal)
admin.site.register(models.TipoAnimal) 