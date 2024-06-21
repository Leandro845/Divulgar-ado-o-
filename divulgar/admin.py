from django.contrib import admin
from .models import Raca, Tag, Pet

# Registering Raca model with the admin interface
admin.site.register(Raca)

# Registering Tag model with the admin interface
admin.site.register(Tag)

# Registering Pet model with the admin interface
admin.site.register(Pet)
