from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import Filme

# Create your views here.
#def homepage(request):
#return render(request, 'homepage.html')


class Homepage(TemplateView):
    template_name= 'homepage.html'


class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme
    # objecy_list

class Detalhesfilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme