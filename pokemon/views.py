from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from pokemon.forms import PokemonForm, PokemonMasterForm

from pokemon.models import Pokemon, PokemonMaster


def main(request):
    context = Pokemon.objects.all()
    return render(request, "pokemon/home.html", {"pokemons": context})


def pokemon(request, pokemon_id):
    if pokemon_id:
        pokemon = Pokemon.objects.get(id=pokemon_id)
        type = pokemon.type.all().first().name
        return render(
            request, "pokemon/pokemon.html", {"pokemon": pokemon, "type": type}
        )
    else:
        return render(request, "pokemon/pokemon.html")


def pokemons(request):
    context = Pokemon.objects.all()
    return render(request, "pokemon/pokemons_list.html", {"pokemons": context})


def masters(request):
    context = PokemonMaster.objects.all()
    print("context", context)
    return render(request, "pokemon/masters_list.html", {"masters": context})


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        pokemons = Pokemon.objects.filter(name__contains=searched)
        return render(
            request, "pokemon/search.html", {"searched": searched, "pokemons": pokemons}
        )
    else:
        return render(request, "pokemon/search.html", {})


def master(request, master_id):
    master = PokemonMaster.objects.get(id=master_id)
    pokemons = master.pokemons.all()
    return render(
        request, "pokemon/master.html", {"master": master, "pokemons": pokemons}
    )


def add_master(request):
    submitted = False
    if request.method == "POST":
        form = PokemonMasterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add-master?submitted=True")
    else:
        form = PokemonMasterForm()
        if "submitted" in request.GET:
            submitted = True
    return render(
        request, "pokemon/master-create.html", {"form": form, "submitted": submitted}
    )


def add_pokemon(request):
    submitted = False
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add-pokemon?submitted=True")
    else:
        form = PokemonForm()
        if "submitted" in request.GET:
            submitted = True
    return render(
        request, "pokemon/pokemon-create.html", {"form": form, "submitted": submitted}
    )
