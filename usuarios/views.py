from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth import authenticate, login, logout

# View function for user registration
def cadastro(request):
    # If the user is already authenticated, redirect to a different page
    if request.user.is_authenticated:
        return redirect('/divulgar/novo_pet')
    
    # If the request method is GET, render the registration page
    if request.method == 'GET':
        return render(request, 'usuarios/cadastro.html')
    
    # If the request method is POST, handle the form submission
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Check if all fields are filled out
        if not nome.strip() and not email.strip() and not senha.strip() and not confirmar_senha.strip():
            messages.add_message(request, constants.ERROR, 'All fields must be filled out')
            return render(request, 'usuarios/cadastro.html')

        # Check if the password and confirmation password match
        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Passwords do not match')
            return render(request, 'usuarios/cadastro.html')

        # Validate the email format
        try:
            validate_email(email)
        except:
            messages.add_message(request, constants.ERROR, 'Invalid email')
            return render(request, 'usuarios/cadastro.html')

        # Attempt to create a new user
        try:
            user = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            messages.add_message(request, constants.SUCCESS, 'User created successfully')
            return render(request, 'usuarios/cadastro.html')
        except:
            messages.add_message(request, constants.ERROR, 'Internal system error')
            return render(request, 'usuarios/cadastro.html')

# View function for user login
def logar(request):
    # If the request method is GET, render the login page
    if request.method == 'GET':
        return render(request, 'usuarios/login.html')
    
    # If the request method is POST, handle the form submission
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')

        # Authenticate the user
        user = authenticate(
            username=nome,
            password=senha
        )

        # If authentication is successful, log the user in and redirect
        if user is not None:
            login(request, user)
            return redirect('/divulgar/novo_pet')
        else:
            # If authentication fails, display an error message
            messages.add_message(request, constants.ERROR, 'Incorrect username or password')
            return render(request, 'usuarios/login.html')

# View function for user logout
def sair(request):
    # Log the user out and redirect to the login page
    logout(request)
    return redirect('/auth/login')
