from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    type = models.ManyToManyField(PokemonType, related_name="pokemon", null=True, blank=True)
    weight = models.IntegerField()
    hp = models.IntegerField()
    attk = models.IntegerField()
    df = models.IntegerField()
    speed = models.IntegerField()
    spe_atk = models.IntegerField(null=True, blank=True)
    spe_df = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class PokemonMaster(models.Model):
    name = models.CharField(max_length=255)
    pokemons = models.ManyToManyField(Pokemon, related_name="pokemon")

    def __str__(self) -> str:
        return self.name
