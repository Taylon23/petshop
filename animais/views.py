from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from . import models
from . import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CreateAnuncio(CreateView):
    form_class = forms.AdicinarAnuncio
    template_name = 'form_animal.html'
    success_url = reverse_lazy('meus-anuncios')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateAnuncio(UpdateView):
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


class DeleteAnuncio(DeleteView):
    form_class = forms.AnimalDeleteForm
    template_name = 'form_delete_animal.html'
    success_url = reverse_lazy('meus-anuncios')

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


def infomacao_anuncio(request, id):
    animal = get_object_or_404(models.Animal, pk=id)
    return render(request, 'infomacao_anuncio.html', {'anuncio_animal': animal})
