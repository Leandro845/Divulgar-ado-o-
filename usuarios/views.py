from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not nome.strip() \
            and not email.strip() \
            and not senha.strip() \
            and not confirmar_senha.strip():
            messages.add_message(request, constants.ERROR, 'Todos os campos tem que serem preenchidos')
            return render(request, 'usuarios/cadastro.html')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não conferem')
            return render(request, 'usuarios/cadastro.html')

        try:
            validate_email(email)
        except:
            messages.add_message(request, constants.ERROR, 'Email inválido')
            return render(request, 'usuarios/cadastro.html')

        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            messages.add_message(request, constants.SUCCESS, 'Usuario criado com sucesso')
            return render(request, 'usuarios/cadastro.html')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return render(request, 'usuarios/cadastro.html')


def logar(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        user = authenticate(
            username=nome,
            password=senha
        )

        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorreto')
            return render(request, 'usuarios/login.html')

def sair(request):
    logout(request)
    return redirect('/auth/login')