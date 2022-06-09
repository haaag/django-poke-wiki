# Trabajo CoderHouse (Django)

Simple Pokemon Wiki

## Instalación Virtual Env.

### Windows

```bash
C:\> python -m venv c:\path\to\myenv
```

### Linux

```bash
python -m virtualenv .venv
```

## Instalación Dependencias

Una vez creado el virtual env, instalar dependencias.

~~~bash
pip install -r requirements.txt
~~~

## Modo de uso

Se debe ejecutar el comando `python manage.py populate` para descargar las imágenes faltantes.

```bash
$ python manage.py populate
```

## Vistas

~~~python
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
~~~
