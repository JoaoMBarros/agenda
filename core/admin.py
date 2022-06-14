from django.contrib import admin
from core.models import Evento

# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    # Configurado para mostrar na tela de admin os campos abaixos
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')

    # Opcao de filtragem na tela de admin
    list_filter = ('usuario', 'data_evento', )

admin.site.register(Evento, EventoAdmin)
