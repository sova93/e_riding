from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class DescriptionStep(models.Model):
    name = models.CharField(max_length=128)
    length = models.FloatField()
    #  step_map = models.ImageField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="description_step_user")


class CustomUser(AbstractUser):
    phone = models.CharField(blank=True, null=True, max_length=20)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        # return "<CustomUser: '%s'>" % (self.username)
        return self.username[:24]


class Horse(models.Model):
    name = models.CharField(max_length=8)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='horse_owner')
    color = models.CharField(max_length=8)
    breed = models.CharField(max_length=8)
    stable = models.CharField(max_length=8)
    birthday = models.DateField()  # field is missing on db scheme

    def __str__(self):
        return "<Horse '%s'>" % (self.name)


class Team(models.Model):  # @TODO: review relations and fields in picture
    name = models.CharField(max_length=20)
    pairs = models.ManyToManyField("Pair", related_name="team_pair")  # connection changed!
     # cosiak so sviaz'u


class VetCard(models.Model):
    user = models.ForeignKey(CustomUser, related_name='vetcard_user')  # cosiak so sviaz'u
    pulse = models.CharField(max_length=3)
    mucouns_membrane = models.CharField(max_length=50)
    capilary_refill = models.CharField(max_length=50)
    dehydratation = models.CharField(max_length=50)
    gut_sounds = models.CharField(max_length=50)
    muscle_tone = models.CharField(max_length=50)
    gait = models.CharField(max_length=2)
    overall = models.CharField(max_length=50)
    notes = models.TextField()
    review_time = models.DateTimeField()


class PairOnStart(models.Model):
    weight_rider = models.FloatField()
    vet_card_on_start = models.ForeignKey(VetCard, blank=True, null=True, related_name='pair_on_start_vet_card')
    cheerleader = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='team_cheerleader')


class Pair(models.Model):
    rider = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='pair_rider')
    horse = models.ForeignKey(Horse, related_name='pair_horse')
    pair_on_start = models.ForeignKey(PairOnStart, related_name='pair_on_start', blank=True, null=True, default=None)

    def __str__(self):
        return "<Pair '%s - %s'>" % (self.rider, self.horse)


class Step(models.Model):
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    vet_entrance_time = models.DateTimeField()
    norm_execution = models.CharField(max_length=100)
    pair = models.ForeignKey(Pair, related_name='step_pair')
    description_step = models.ForeignKey(DescriptionStep, related_name='step_description_step')
    vet_card = models.ForeignKey(VetCard, related_name='step_vet_card')


class Competition(models.Model):
    begin = models.DateTimeField()
    close = models.DateTimeField()
    place = models.CharField(max_length=100)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='competition_manager')
    teams = models.ManyToManyField(Team, related_name='competition_teams')
    judges = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='competition_judges')


class News(models.Model):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to="news_images/")
    datetime = models.DateTimeField()
    content = models.TextField()
