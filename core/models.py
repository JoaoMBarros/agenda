from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Classe com os atribulos de cada evento
class Evento(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(blank = True, null = True)
    data_evento = models.DateTimeField(verbose_name = 'Data do evento')
    data_criacao = models.DateTimeField(auto_now = True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    

    class Meta():
        db_table = 'evento'

    def __str__(self):
        return self.titulo
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        return False
    
    def get_evento_proximo(self):
        atraso = self.data_evento - datetime.now()
        if atraso > timedelta(hours=0) and atraso <= timedelta(hours=1):
            return True
        return False