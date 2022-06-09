import django
django.setup()
from dataclasses import dataclass
import json
import requests
from time import sleep

from .models import PokemonType
#
# used_type = set(PokemonType.objects.values_list('text', flat=True))
# print(used_type)

# from pokemon.models import PokemonMaster, Pokemon, PokemonType

# file = "./sample.json"
#
# with open(file) as json_file:
#     poke_json = json.load(json_file)
#
#
# @dataclass
# class PokemonJSON:
#     name: str
#     abilities: list[str]
#     type: str
#     stats: list[dict[str, str]]
#
#
def generate_request(url: str):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


#
#
# poke_ids = range(1, 100)
# types_pokemos = {
#     "psychic",
#     "ghost",
#     "ground",
#     "bug",
#     "grass",
#     "normal",
#     "fire",
#     "fighting",
#     "rock",
#     "electric",
#     "fairy",
#     "poison",
#     "water",
# }
#
#
#
# poke_ids = range(1, 100)
poke_ids = range(1, 20)
for pkid in poke_ids:

    response = generate_request(url=f"https://pokeapi.co/api/v2/pokemon/{pkid}")
    json_object = json.dumps(response, indent=4)
    data = json.loads(json_object)
    #
    name = data["forms"][0]["name"]
    print(name)
    type = data["types"][0]["type"]["name"]
    abilities = [abilitie["ability"]["name"] for abilitie in data["abilities"]]
    # img_url = data["sprites"]["other"]["official-artwork"]["front_default"]
    img_url = data["sprites"]["front_default"]

    r = requests.get(img_url, stream=True)
    if r.status_code == 200:
        with open(f"./{name}.png", 'wb') as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)

    stats_list = []
    for stat in data["stats"]:
        base_stat = stat["base_stat"]
        name_stat = stat["stat"]["name"]
        dict_stat = {"name": name_stat, "base": base_stat}
        print("stat name", name_stat)
        print("stat base", base_stat)
        stats_list.append(dict_stat)

    # pokemon = PokemonJSON(name, abilities, type, stats_list)
    # print(pokemon.stats)
    sleep(0.2)
    break
