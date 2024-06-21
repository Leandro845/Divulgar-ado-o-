from django.urls import path
from . import views

urlpatterns = [
    # Path for listing pets available for adoption
    path('', views.listar_pets, name='listar_pets'),

    # Path for initiating adoption request for a specific pet identified by id_pet
    path('pedido_adocao/<int:id_pet>', views.pedido_adocao, name='pedido_adocao'),

    # Path for processing adoption request identified by id_pedido (approve or reject)
    path('processa_pedido_adocao/<int:id_pedido>', views.processa_pedido_adocao, name='processa_pedido_adocao')
]
