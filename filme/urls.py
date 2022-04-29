# url - views - template
from django.contrib.auth import views as auth_view
from django.urls import path, include
from .views import (
    Homepage, 
    Homefilmes, 
    Detalhesfilme,
    PesquisaFilme,
    PaginaPerfil,
    CriarConta
)


app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>', Detalhesfilme.as_view(), name="detalhesfilme"),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme' ),
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/', PaginaPerfil.as_view(), name='editarperfil'),
    path('criarconta/', CriarConta.as_view(), name='criarconta'),
]

# Comentario