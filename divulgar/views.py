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
        tags = Tag.objects.all()
        racas = Tag.objects.all()
        return render(request, 'divulgar/novo_pet.html', {'tags': tags, 'racas': racas})
    elif request.method == 'POST':
        foto = request.FILES.get('foto')
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        telefone = request.POST.get('telefone')
        tags = request.POST.getlist('tags')
        raca = request.POST.get('raca')

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

        if not foto:
            messages.add_message(request, constants.ERROR, 'É obrigatorio preencher o campo de imagem')
            tags = Tag.objects.all()
            racas = Tag.objects.all()
            return render(request, 'divulgar/novo_pet.html', {'tags': tags, 'racas': racas})

        if not foto \
            and not nome \
            and not descricao \
            and not estado \
            and not cidade \
            and not telefone \
            and not tags \
            and not raca:
            messages.add_message(request, constants.ERROR, 'Nenhum campo foi preenchido')
            tags = Tag.objects.all()
            racas = Tag.objects.all()
            return render(request, 'divulgar/novo_pet.html', {'tags': tags, 'racas': racas})


        pet.save()

        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            pet.tags.add(tag)

        pet.save()

        return redirect('novo_pet')

@login_required
def seus_pet(request):
    if request.method == 'GET':
        pets = Pet.objects.filter(usuario=request.user)
        return render(request, 'divulgar/seus_pet.html', {'pets': pets})

@login_required
def remover_pet(request, id):
    pet = Pet.objects.get(id=id)

    if pet.usuario != request.user:
        messages.add_message(request, constants.ERROR, 'Esse pet não é seu')
        return redirect('seus_pet')

    pet.delete()

    messages.add_message(request, constants.SUCCESS, 'Pet removido com sucesso')
    return redirect('seus_pet')

@login_required
def ver_pet(request, id):
    if request.method == 'GET':
        pet = Pet.objects.get(id=id)
        return render(request, 'divulgar/ver_pet.html', {'pet': pet})

@login_required
def ver_pedido_adocao(request):
    if request.method == 'GET':
        pedidos = PedidoAdocao.objects.filter(usuario=request.user).filter(status='AG')
        return render(request, 'divulgar/ver_pedido_adocao.html', {'pedidos': pedidos})


def dashboard(request):
    if request.method == 'GET':
        return render(request, 'divulgar/dashboard.html')

@csrf_exempt
def api_adocoes_por_raca(request):
    racas = Raca.objects.all()

    qtd_adocoes = []
    for raca in racas:
        adocoes = len(PedidoAdocao.objects.filter(pet__raca=raca))
        qtd_adocoes.append(adocoes)

    racas = [raca.raca for raca in racas]
    data = {'qtd_adocoes': qtd_adocoes, 'labels': racas}

    return JsonResponse(data)



