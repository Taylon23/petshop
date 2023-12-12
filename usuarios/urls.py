from django.urls import path
from . import views
from django.contrib.auth import views as Authviews


urlpatterns = [
    path('login/',Authviews.LoginView.as_view(template_name='form_auth.html'),name="login"),
    path('singup/', views.signup,name="singup"),
    path('logout/',Authviews.LogoutView.as_view(template_name='form_auth.html'),name="logout"),
    path('meus-anuncios/', views.meus_anuncios, name='meus-anuncios'),
    path('favoritar-animal/<int:animal_id>/',
         views.favoritar_animal, name='favoritar_animal'),
    path('favoritos/', views.meus_favoritos, name='meus-favoritos'),
]
