from django.db import models
from django.contrib.auth.models import AbstractUser


class DescriptionStep(models.Model):
    length = models.FloatField()
    #  step_map = models.ImageField()


class CustomUser(AbstractUser):
    phone = models.TextField()
    birthday = models.DateField()


class Horse(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(CustomUser)
    color = models.TextField()
    breed = models.TextField()
    stable = models.TextField()


class Team(models.Model):
    rider = models.ForeignKey(CustomUser, related_name='rider_user')
    horse = models.ForeignKey(Horse)
    cheerleader = models.ForeignKey(CustomUser, related_name='cheerleader_user')  # cosiak so sviaz'u


class VetCard(models.Model):
    user = models.ForeignKey(CustomUser)  # cosiak so sviaz'u
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
    team = models.ForeignKey(Team)
    rider = models.ForeignKey(CustomUser)
    horse = models.ForeignKey(Horse)
    weight_rider = models.FloatField()
    vet_card_on_start = models.ForeignKey(VetCard)


class Step(models.Model):
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    vet_entrance_time = models.DateTimeField()
    norm_execution = models.TextField()
    pair = models.ForeignKey(Pair)
    description_step = models.ForeignKey(DescriptionStep)
    vet_card = models.ForeignKey(VetCard)
