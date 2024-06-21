from django.db import models
from django.contrib.auth.models import User

# Model to represent the breed of the pet
class Raca(models.Model):
    raca = models.CharField(max_length=50)

    def __str__(self):
        return self.raca

# Model to represent tags associated with pets
class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag

# Main model to represent a pet
class Pet(models.Model):
    # Choices for the status of the pet
    choice_status = (
        ('P', 'For adoption'),
        ('A', 'Adopted')
    )
    # Foreign key to the user who owns the pet
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # Pet's photo
    foto = models.ImageField(upload_to='pet_photos')
    # Pet's name
    nome = models.CharField(max_length=100)
    # Pet's description
    descricao = models.TextField()
    # State where the pet is located
    estado = models.CharField(max_length=50)
    # City where the pet is located
    cidade = models.CharField(max_length=50)
    # Contact phone number related to the pet
    telefone = models.CharField(max_length=14)
    # Tags associated with the pet
    tags = models.ManyToManyField(Tag)
    # Breed of the pet
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    # Current status of the pet (For adoption or Adopted)
    status = models.CharField(max_length=1, choices=choice_status, default='P')

    def __str__(self):
        return self.nome
