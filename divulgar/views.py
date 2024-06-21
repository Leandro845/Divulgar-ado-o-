from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Tag, Raca, Pet
from django.contrib import messages
from django.contrib.messages import constants
from adotar.models import PedidoAdocao
from django.views.decorators.csrf import csrf_exempt

@login_required
def novo_pet(request):
    if request.method == 'GET':
        # Retrieve all tags and breeds (racas) from the database
        tags = Tag.objects.all()
        racas = Raca.objects.all()
        # Render the 'novo_pet.html' template with the retrieved data
        return render(request, 'divulgar/novo_pet.html', {'tags': tags, 'racas': racas})
    elif request.method == 'POST':
        # Retrieve form data from POST request
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        raca = request.POST.get('raca')

        # Create a new Pet object with retrieved data
        pet = Pet(
            usuario=request.user,
            foto=foto,
            nome=nome,
            descricao=descricao,
            estado=estado,
            cidade=cidade,
            telefone=telefone,
            raca_id=raca
        )

        # Validate if 'foto' field is provided
        if not foto:
            messages.add_message(request, constants.ERROR, 'É obrigatório preencher o campo de imagem')
            tags = Tag.objects.all()
            racas = Raca.objects.all()
            return render(request, 'divulgar/novo_pet.html', {'tags': tags, 'racas': racas})

        # Validate if all required fields are filled
        if not foto and not nome and not descricao and not estado and not cidade and not telefone and not tags and not raca:
            messages.add_message(request, constants.ERROR, 'Nenhum campo foi preenchido')
            tags = Tag.objects.all()
            racas = Raca.objects.all()
            return render(request, 'divulgar/novo_pet.html', {'tags': tags, 'racas': racas})

        # Save the pet object to the database
        pet.save()

        # Add tags to the pet
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)

        pet.save()

        # Redirect to 'novo_pet' page after successful submission
        return redirect('novo_pet')

@login_required
def seus_pet(request):
    if request.method == 'GET':
        # Retrieve all pets belonging to the current user
        pets = Pet.objects.filter(usuario=request.user)
        # Render the 'seus_pet.html' template with the retrieved pets
        return render(request, 'divulgar/seus_pet.html', {'pets': pets})

@login_required
def remover_pet(request, id):
    # Retrieve the pet object by ID
    pet = Pet.objects.get(id=id)

    # Check if the pet belongs to the current user
    if pet.usuario != request.user:
        messages.add_message(request, constants.ERROR, 'Esse pet não é seu')
        return redirect('seus_pet')

    # Delete the pet object from the database
    pet.delete()

    # Display success message and redirect to 'seus_pet'
    messages.add_message(request, constants.SUCCESS, 'Pet removido com sucesso')
    return redirect('seus_pet')

@login_required
def ver_pet(request, id):
    if request.method == 'GET':
        # Retrieve a specific pet object by ID
        pet = Pet.objects.get(id=id)
        # Render the 'ver_pet.html' template with the retrieved pet
        return render(request, 'divulgar/ver_pet.html', {'pet': pet})

@login_required
def ver_pedido_adocao(request):
    if request.method == 'GET':
        # Retrieve adoption requests where the current user is the requester and status is 'AG' (Agendado)
        pedidos = PedidoAdocao.objects.filter(usuario=request.user).filter(status='AG')
        # Render the 'ver_pedido_adocao.html' template with the retrieved adoption requests
        return render(request, 'divulgar/ver_pedido_adocao.html', {'pedidos': pedidos})

def dashboard(request):
    if request.method == 'GET':
        # Render the 'dashboard.html' template
        return render(request, 'divulgar/dashboard.html')

@csrf_exempt
def api_adocoes_por_raca(request):
    # Retrieve all races (racas)
    racas = Raca.objects.all()

    # Calculate the number of adoptions for each race
    qtd_adocoes = []
    for raca in racas:
        adocoes = len(PedidoAdocao.objects.filter(pet__raca=raca))
        qtd_adocoes.append(adocoes)

    # Extract race names (racas) for labels
    racas = [raca.raca for raca in racas]

    # Prepare JSON response data with adoption quantities and labels
    data = {'qtd_adocoes': qtd_adocoes, 'labels': racas}

    # Return JSON response
    return JsonResponse(data)




