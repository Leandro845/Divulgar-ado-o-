from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for creating a new pet
    path('novo_pet/', views.novo_pet, name='novo_pet'),

    # URL pattern for listing user's pets
    path('seus_pet/', views.seus_pet, name='seus_pet'),

    # URL pattern for removing a pet by its ID
    path('remover_pet/<int:id>/', views.remover_pet, name='remover_pet'),

    # URL pattern for viewing details of a specific pet by its ID
    path('ver_pet/<int:id>/', views.ver_pet, name='ver_pet'),

    # URL pattern for viewing adoption requests for the current user
    path('ver_pedido_adocao/', views.ver_pedido_adocao, name='ver_pedido_adocao'),

    # URL pattern for the dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # URL pattern for the API endpoint to get adoptions by race
    path('api_adocoes_por_raca/', views.api_adocoes_por_raca, name='api_adocoes_por_raca'),
]



