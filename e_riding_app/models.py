from django.db import models
from django.contrib.auth.models import AbstractUser


class DescriptionStep(models.Model):
    length = models.FloatField()
    #  step_map = models.ImageField()


class CustomUser(AbstractUser):
    phone = models.TextField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)


class Horse(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(CustomUser, related_name='horse_owner')
    color = models.TextField()
    breed = models.TextField()
    stable = models.TextField()


class Team(models.Model):
    rider = models.ForeignKey(CustomUser, related_name='team_rider')
    horse = models.ForeignKey(Horse, related_name='team_horse')
    cheerleader = models.ManyToManyField(CustomUser, related_name='team_cheerleader')  # cosiak so sviaz'u


class VetCard(models.Model):
    user = models.ForeignKey(CustomUser, related_name='vetcard_user')  # cosiak so sviaz'u
    pulse = models.TextField()
    mucouns_membrane = models.TextField()
    capilary_refill = models.TextField()
    dehydratation = models.TextField()
    gut_sounds = models.TextField()
    muscle_tone = models.TextField()
    gait = models.TextField()
    overall = models.TextField()
    notes = models.TextField()
    review_time = models.DateTimeField()


class Pair(models.Model):
    team = models.ForeignKey(Team, related_name='pair_team')
    rider = models.ForeignKey(CustomUser, related_name='pair_rider')
    horse = models.ForeignKey(Horse, related_name='pair_horse')
    weight_rider = models.FloatField()
    vet_card_on_start = models.ForeignKey(VetCard, related_name='pair_vet_card_on_start')


class Step(models.Model):
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    vet_entrance_time = models.DateTimeField()
    norm_execution = models.TextField()
    pair = models.ForeignKey(Pair, related_name='step_pair')
    description_step = models.ForeignKey(DescriptionStep, related_name='step_description_step')
    vet_card = models.ForeignKey(VetCard, related_name='step_vet_card')


class Competition(models.Model):
    begin = models.DateTimeField()
    close = models.DateTimeField()
    place = models.TextField()
    manager = models.ForeignKey(CustomUser, related_name='competition_manager')
    teams = models.ManyToManyField(Team, related_name='competition_teams')
    judges = models.ManyToManyField(CustomUser, related_name='competition_judges')
