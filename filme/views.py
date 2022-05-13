from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from .forms import CriarContaForm, FormHomePage
from tempfile import template
from .models import Filme, Usuario

from django.views.generic import (
    TemplateView, 
    ListView, 
    DetailView,
    FormView,
    UpdateView
)

# Create your views here.
#def homepage(request):
#return render(request, 'homepage.html')


class Homepage(FormView):
    template_name= 'homepage.html'
    form_class = FormHomePage

    def get(self, request, *args, **kwargs): # Condiçoes para usuarios logados
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs) # Para a homepage

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email=email)
        if usuario:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme
    # objecy_list

class Detalhesfilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme


    def get(self, request, *args, **kwargs): # Contador de visualizações
        filme = self.get_object()
        filme.visualizacao += 1
        filme.save()
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs) # redireciona para a URL final 


    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filme_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filme_relacionados
        return context


class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        pesquisa = self.request.GET.get('query')
        if pesquisa:
            object_list = Filme.objects.filter(titulo__icontains=pesquisa)
            return object_list
        else:
            return 'Erro'


class PaginaPerfil(LoginRequiredMixin, UpdateView): #UpdateView vai atualizar as informações
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')
