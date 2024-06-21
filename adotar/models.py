from django.db import models
from divulgar.models import Pet  # Importing the Pet model from 'divulgar' app
from django.contrib.auth.models import User  # Importing Django's built-in User model


class PedidoAdocao(models.Model):
    # Choices for status field
    choices_status = (
        ('AG', 'Aguardando aprovação'),  # Waiting for approval
        ('AP', 'Aprovado'),              # Approved
        ('R', 'Recusado')                # Rejected
    )
    
    # Foreign key to Pet model, on_delete specifies behavior if referenced Pet is deleted
    pet = models.ForeignKey(Pet, on_delete=models.DO_NOTHING)
    
    # Foreign key to User model, represents the user making the adoption request
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    # Date and time when the adoption request was made
    data = models.DateTimeField()
    
    # Status of the adoption request, using choices defined above, default is 'AG' (waiting for approval)
    status = models.CharField(max_length=2, choices=choices_status, default='AG')

    def __str__(self):
        return self.pet.nome  # String representation of PedidoAdocao instance returns the pet's name
