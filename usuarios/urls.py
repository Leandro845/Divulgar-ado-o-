from django.urls import path
from . import views

# Define urlpatterns to map URLs to view functions
urlpatterns = [
    # URL pattern for user registration
    path('cadastro/', views.cadastro, name='cadastro'),

    # URL pattern for user login
    path('login/', views.logar, name='login'),

    # URL pattern for user logout
    path('sair/', views.sair, name='sair'),
]
