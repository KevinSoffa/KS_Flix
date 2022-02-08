from tempfile import template
from django.shortcuts import render
from .models import Filme
from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView,
    )

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


    def get(self, request, *args, **kwargs): # Contador de visualizações
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        return super().get(request, *args, **kwargs) # redireciona para a URL final 


    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filme_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filme_relacionados
        return context


class PesquisaFilme(ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        pesquisa = self.request.GET.get('query')
        if pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=pesquisa)
            return object_list
        else:
            return 'Erro'
