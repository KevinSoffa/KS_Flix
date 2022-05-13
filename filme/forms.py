from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms


class CriarContaForm(UserCreationForm):
    email = forms.EmailField()


class FormHomePage(forms.Form):
    email = forms.EmailField(label=False)


    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')

