from django.forms import ModelForm, TextInput
from .models import *
from django.contrib.auth.models import User
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserAddForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["username","first_name","last_name","email","phone","birthday","groups", 'password']
        widgets = {
            "birthday": TextInput(attrs={'type': 'date'}),
            "password": TextInput(attrs={'type': 'password'})
        }
        help_texts = {
            "username": "Обязательно. 150 символов или меньше. Разрешены: буквы, цифры и @/./+/-/_.",
            "groups": ""

        }
        labels = {
            "username": "Имя пользователя",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "email": "E-Mail адрес",
            "phone": "Номер телефона",
            "birthday": "День рождения",
            "groups": "Роль",
            "password": "Пароль",
        }

    def __init__(self, *args, **kwargs):
        super (UserAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-8'
        self.helper.attrs

        self.helper.add_input(Submit('submit', 'Зарегестрироваться'))


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
