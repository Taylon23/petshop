from django.urls import path
from . import views


urlpatterns = [
    path('meus-anuncios/',views.meus_anuncios,name='meus-anuncios')
]