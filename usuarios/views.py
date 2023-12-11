from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from animais import models
from . import models as models_user
from django.core.paginator import Paginator


def meus_anuncios(request):
    anuncios_list = models.Animal.objects.filter(user=request.user)

    # Dividindo em páginas, 10 itens por página
    paginator = Paginator(anuncios_list, 8)
    # Obtendo o número da página da query string, padrão é a página 1
    page_number = request.GET.get('page')

    # Obtendo os objetos da página atual
    page_obj = paginator.get_page(page_number)

    return render(request, 'meus_anuncios.html', {'page_obj': page_obj})

def meus_favoritos(request):
    favoritos = models_user.Favorito.objects.filter(usuario=request.user)
    # Dividindo em páginas, 10 itens por página
    paginator = Paginator(favoritos, 8)
    # Obtendo o número da página da query string, padrão é a página 1
    page_number = request.GET.get('page')

    # Obtendo os objetos da página atual
    page_obj = paginator.get_page(page_number)
    return render(request, 'anuncios_favoritos.html',{'page_obj': page_obj})


def favoritar_animal(request, animal_id):
    animal = get_object_or_404(models.Animal, pk=animal_id)
    
    if request.user.is_authenticated:
        favorito, created = models_user.Favorito.objects.get_or_create(usuario=request.user, animal=animal)
        if not created:
            favorito.delete()
        animal.favoritado = not animal.favoritado
        animal.save()
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Usuário não autenticado'})
