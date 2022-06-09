from django import forms
from django.forms import ModelForm
from .models import PokemonMaster, Pokemon, PokemonType


class PokemonMasterForm(forms.ModelForm):
    class Meta:
        model = PokemonMaster
        fields = ("name", "pokemons")
        labels = {"name": ""}

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre Entrenador"}
            ),
        }


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return "%s" % member.name


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ("name", "weight", "hp", "attk", "df", "speed")
        labels = {
            "name": "",
            "type": "",
            "weight": "",
            "hp": "",
            "attk": "",
            "df": "",
            "speed": "",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre"}
            ),
            "weight": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Peso (kg)"}
            ),
            "hp": forms.TextInput(attrs={"class": "form-control", "placeholder": "HP"}),
            "attk": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ataque"}
            ),
            "df": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Defensa"}
            ),
            "speed": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Velocidad"}
            ),
        }

    tipos = CustomMMCF(
        queryset=PokemonType.objects.all(), widget=forms.CheckboxSelectMultiple
    )
