from django.shortcuts import redirect, render
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

# Funcao de login do usuário
def login_user(request):
    return render(request, 'login.html')

# Funcao de logout do usuário
def logout_user(request):
    logout(request)
    return redirect('/') #O redirect '/' retorna a pagina inicial, que por sua vez redireciona para a /agenda/

# Funcao que verifica o login de usuário
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password) #A funcao authenticate verifica se o usuario e senha sao validos
        if usuario is not None: # Se o usuario nao for none, ou seja, a funcao authenticate retornou um valor valido, o login acontece
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou senha invalidos")
    return redirect('/')

# Listagem de todos os eventos do usuário logado 
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

# Funcao que retorna os detalhes de cada evento
@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

# Controle da criacao de um novo evento
@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.data_evento = data_evento
                evento.descricao = descricao
                evento.save()
        else:
            Evento.objects.create(titulo=titulo,
                                data_evento=data_evento,
                                descricao=descricao,
                                usuario=usuario)
    return redirect('/')

# Controle da exclusao de um evento
@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')