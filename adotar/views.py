from django.shortcuts import render, redirect, get_object_or_404
from divulgar.models import Pet, Raca
from django.contrib import messages
from .models import PedidoAdocao
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.messages import constants

@login_required
def listar_pets(request):
    """
    View function to list pets available for adoption, optionally filtered by city and breed.

    Parameters:
    - request: HTTP request object

    Returns:
    - Rendered template with filtered pets list
    """
    if request.method == 'GET':
        pets = Pet.objects.filter(status='P')
        racas = Raca.objects.all()

        cidade = request.GET.get('cidade')
        raca_filter = request.GET.get('raca')

        # Filter pets by city if provided
        if cidade:
            pets = pets.filter(cidade__icontains=cidade)

        # Filter pets by breed if provided
        if raca_filter:
            pets = pets.filter(raca__id=raca_filter)
            raca_filter = Raca.objects.get(id=raca_filter)

        return render(request, 'adotar/listar_pets.html',
                      {'pets': pets, 'racas': racas, 'cidade': cidade, 'raca_filter': raca_filter}
                      )

@login_required
def pedido_adocao(request, id_pet):
    """
    View function to process adoption requests for a specific pet.

    Parameters:
    - request: HTTP request object
    - id_pet: ID of the pet for adoption

    Returns:
    - Redirect to the adoption page with success or warning message
    """
    pet = get_object_or_404(Pet, id=id_pet, status='P')

    # Create a new adoption request
    pedido = PedidoAdocao(
        pet=pet,
        usuario=request.user,
        data=datetime.now()
    )

    pedido.save()
    messages.success(request, 'Adoption request successfully submitted')
    return redirect('/adotar')

@login_required
def processa_pedido_adocao(request, id_pedido):
    """
    View function to process adoption requests (approve or reject).

    Parameters:
    - request: HTTP request object
    - id_pedido: ID of the adoption request to process

    Returns:
    - Redirect to the adoption request view with success message
    """
    status = request.GET.get('status')
    pedido = PedidoAdocao.objects.get(id=id_pedido)

    if status == 'A':
        # Approve adoption request
        pet = pedido.pet
        pet.status = 'A'
        pet.save()
        pedido.status = 'AP'
        string = 'Hello, your adoption has been approved...'
    elif status == 'R':
        # Reject adoption request
        pedido.status = 'R'
        string = 'Hello, your adoption has been rejected...'

    pedido.save()

    # Send email notification
    email = send_mail(
        'Your adoption request has been processed',
        string,
        'youremail@example.com',
        [pedido.usuario.email,]
    )

    messages.success(request, 'Adoption request processed successfully')
    return redirect('ver_pedido_adocao')
