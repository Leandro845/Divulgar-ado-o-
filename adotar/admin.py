from django.contrib import admin
from .models import PedidoAdocao  # Importing the PedidoAdocao model from current package (assuming it's in the same directory)

# Registering the PedidoAdocao model with the Django admin site
admin.site.register(PedidoAdocao)
