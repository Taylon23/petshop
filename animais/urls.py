from django.urls import path
from . import views


urlpatterns = [
    path('adicionar-anuncio/',views.CreateAnuncio.as_view(),name='adicionar-anuncio'),
    path('atualizar-anuncio/<int:pk>',views.UpdateAnuncio.as_view(),name='atualizar-anuncio'),
    path('deletar-anuncio/<int:pk>',views.DeleteAnuncio.as_view(),name='deletar-anuncio'),
]