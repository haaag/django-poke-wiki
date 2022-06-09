from django.urls import path
from pokemon import views

urlpatterns = [
    path('', views.main, name='Index'),
    path('pokemon/<pokemon_id>', views.pokemon, name='pokemon-view'),
    path('search/', views.search, name="search"),
    path('pokemons/', views.pokemons, name='pokemons-list'),
    path('masters/', views.masters, name='masters-list'),
    path('master/<master_id>', views.master, name='master-detail'),
    path('add-master', views.add_master, name='create-master'),
    path('add-pokemon', views.add_pokemon, name='create-pokemon')
]
