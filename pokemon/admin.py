from django.contrib import admin
from .models import Pokemon, PokemonMaster, PokemonType

# Register your models here.

admin.site.register(Pokemon)
admin.site.register(PokemonMaster)
admin.site.register(PokemonType)
