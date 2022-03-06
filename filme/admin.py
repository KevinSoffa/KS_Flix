from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import (
    Filme, 
    Episodio, 
    Usuario
)

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {"fields": ("filmes_vistos",)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Usuario, UserAdmin)
admin.site.register(Filme)
admin.site.register(Episodio)
