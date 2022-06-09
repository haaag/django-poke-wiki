import os
import json
from time import sleep

from poke_wiki.settings import STATICFILES_DIRS

from django.core.management.base import BaseCommand
import requests

from pokemon.models import Pokemon, PokemonType


def generate_request(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


class Command(BaseCommand):
    help = "import pokemons images"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        print("Descargando imagenes de Pokemons.")

        poke_ids = range(1, 51)
        TARGET_DIR = os.path.join(STATICFILES_DIRS[0], 'images/pokemons/')

        for pkid in poke_ids:
            response = generate_request(url=f"https://pokeapi.co/api/v2/pokemon/{pkid}")
            json_object = json.dumps(response, indent=4)
            data = json.loads(json_object)

            name = data["forms"][0]["name"]
            img_url = data["sprites"]["other"]["official-artwork"]["front_default"]

            r = requests.get(img_url, stream=True)
            if r.status_code == 200:
                with open(f"{TARGET_DIR}/{name}.png", "wb") as f:
                    print(f"Downloading: {name}.png")
                    for chunk in r.iter_content(1024):
                        f.write(chunk)

        print("Ya puedes ejecutar: 'python manage.py runserver'")
