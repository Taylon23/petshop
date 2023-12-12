from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from . import models
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from usuarios import models as models_user
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CreateAnuncio(LoginRequiredMixin,CreateView):
    form_class = forms.AdicinarAnuncio
    template_name = 'form_animal.html'
    success_url = reverse_lazy('meus-anuncios')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateAnuncio(LoginRequiredMixin,UpdateView):
    form_class = forms.AdicinarAnuncio
    template_name = 'form_animal.html'
    success_url = reverse_lazy('meus-anuncios')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = get_object_or_404(
            models.Animal, pk=self.kwargs['pk'], user=self.request.user)
        return obj

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # Preencher com a instância existente do modelo
        kwargs['instance'] = self.get_object()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_img_url'] = self.get_object().img_animal.url
        return context


class DeleteAnuncio(LoginRequiredMixin,DeleteView):
    model = models.Animal
    template_name = 'form_delete_animal.html'
    success_url = reverse_lazy('meus-anuncios')

    def get_object(self, queryset=None):
        obj = get_object_or_404(
            models.Animal, pk=self.kwargs['pk'], user=self.request.user)
        return obj

def infomacao_anuncio(request, id):
    animal = get_object_or_404(models.Animal, pk=id)
    esta_favoritado = False  # Inicialmente, assume que não está favoritado

    if request.user.is_authenticated:
        # Verifica se o animal está na lista de favoritos do usuário logado
        esta_favoritado = models_user.Favorito.objects.filter(
            usuario=request.user, animal=animal).exists()

    return render(request, 'infomacao_anuncio.html', {'anuncio_animal': animal, 'esta_favoritado': esta_favoritado})


def search_animal(request):
    query = request.GET.get('q')
    animais = models.Animal.objects.all()

    if query:
        search_words = query.split()  # Separar as palavras da consulta do usuário
        q_objects = Q()  # Inicializar um objeto de consulta vazio

        for word in search_words:
            # Para cada palavra na consulta, adicionar uma condição OR
            q_objects |= (
                Q(titulo__icontains=word) |
                Q(animal__tipo_animal__icontains=query)
            )

        # Aplicar a consulta combinada usando OR para todas as palavras
        animais = animais.filter(q_objects)

    paginator = Paginator(animais, 10)
    page_number = request.GET.get('page')

    try:
        animais = paginator.page(page_number)
    except PageNotAnInteger:
        animais = paginator.page(1)
    except EmptyPage:
        animais = paginator.page(paginator.num_pages)

    return render(request, 'search_results_animal.html', {'page_obj': animais, 'query': query})
