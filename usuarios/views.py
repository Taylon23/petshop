from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from animais import models
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignUpForm
from . import models as models_user
from django.core.paginator import Paginator


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'singup.html', {'form': form})


@login_required(login_url='login')
def meus_anuncios(request):
    anuncios_list = models.Animal.objects.filter(user=request.user)

    # Dividindo em páginas, 10 itens por página
    paginator = Paginator(anuncios_list, 8)
    # Obtendo o número da página da query string, padrão é a página 1
    page_number = request.GET.get('page')

    # Obtendo os objetos da página atual
    page_obj = paginator.get_page(page_number)

    return render(request, 'meus_anuncios.html', {'page_obj': page_obj})


@login_required(login_url='login')
def meus_favoritos(request):
    favoritos = models_user.Favorito.objects.filter(usuario=request.user)
    # Dividindo em páginas, 10 itens por página
    paginator = Paginator(favoritos, 8)
    # Obtendo o número da página da query string, padrão é a página 1
    page_number = request.GET.get('page')

    # Obtendo os objetos da página atual
    page_obj = paginator.get_page(page_number)
    return render(request, 'anuncios_favoritos.html', {'page_obj': page_obj})


@login_required(login_url='login')
def favoritar_animal(request, animal_id):
    animal = get_object_or_404(models.Animal, pk=animal_id)

    if request.user.is_authenticated:
        favorito, created = models_user.Favorito.objects.get_or_create(
            usuario=request.user, animal=animal)
        if not created:
            favorito.delete()
        animal.favoritado = not animal.favoritado
        animal.save()
        return JsonResponse({'status': 'ok'})
    else:
        login_url = reverse('login')  # Obtém a URL de login
        return JsonResponse({'status': 'error', 'message': 'Usuário não autenticado', 'login_url': login_url})
