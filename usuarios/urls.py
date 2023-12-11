from django.urls import path
from . import views


urlpatterns = [
    path('meus-anuncios/', views.meus_anuncios, name='meus-anuncios'),
    path('favoritar-animal/<int:animal_id>/',
         views.favoritar_animal, name='favoritar_animal'),
    path('favoritos/', views.meus_favoritos, name='meus-favoritos'),
]
