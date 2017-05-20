from django.forms import ModelForm, TextInput
from .models import *
from django.contrib.auth.models import User
from django import forms


class UserAddForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username","first_name","last_name","email","phone","birthday","groups", 'password']
        widgets = {"birthday": TextInput(attrs={"readonly":'', 'onfocus': "this.removeAttribute('readonly')",'type':'date'}),
                   "phone":TextInput(attrs={"readonly":'', 'onfocus': "this.removeAttribute('readonly')"}),
                   "password": TextInput(attrs={'autocomplete': 'off', "readonly":'', 'onfocus': "this.removeAttribute('readonly')",'type':'password'})
                   }


class StepForm(ModelForm):
    class Meta:
        model = Step
        exclude = []


class VetCardForm(ModelForm):
    class Meta:
        model = VetCard
        exclude = []


class CompetitionAddForm(ModelForm):
    class Meta:
        model = Competition
        exclude = []


class DescriptionStepAddForm(ModelForm):
    class Meta:
        model = DescriptionStep
        exclude = []


class HorseAddForm(ModelForm):
    class Meta:
        model = Horse
        exclude = []
        labels = {
            "name": "ИМЯ"
        }


class PairAddForm(ModelForm):
    class Meta:
        model = Pair
        exclude = []
        labels = {
            "rider": "Всадник",
            "horse": "Лошадь",
        }


class TeamAddForm(ModelForm):
    class Meta:
        model = Team
        exclude = []
        labels = {
            # "rider": "Всадник",
            # "horse": "Лошадь",
            # "cheerleader": "Команда поддержки"
        }


class PairOnStartAddForm(ModelForm):
    class Meta:
        model = PairOnStart
        exclude = []
        labels = {
            "weight_rider": "Вес всадника",
            "vet_card_on_start": "Веткарта",
            "cheerleader": "Группа поддержки",
        }
