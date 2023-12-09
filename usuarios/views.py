from django.shortcuts import render
from animais import models
from django.core.paginator import Paginator



def meus_anuncios(request):
    anuncios_list = models.Animal.objects.filter(user=request.user)
    
    paginator = Paginator(anuncios_list, 10)  # Dividindo em páginas, 10 itens por página
    page_number = request.GET.get('page')  # Obtendo o número da página da query string, padrão é a página 1
    
    page_obj = paginator.get_page(page_number)  # Obtendo os objetos da página atual
    
    return render(request, 'meus_anuncios.html', {'page_obj': page_obj})
