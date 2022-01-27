# url - views - template

from .views import homepage, homefilmes
from django.urls import path, include


urlpatterns = [
    path('', homepage),
    path('filmes/', homefilmes),
]