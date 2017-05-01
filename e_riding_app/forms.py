from django.forms import ModelForm
from .models import *


class CompetitionAddForm(ModelForm):
    class Meta:
        model = Competition
        exclude = []


class DescriptionStepForm(ModelForm):
    class Meta:
        model = Step
        exclude = []


class HorseFormAdd(ModelForm):
    class Meta:
        model = Horse
        exclude = []
        labels = {
            "name": "ИМЯ"
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