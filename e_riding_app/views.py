from django.shortcuts import render, redirect, get_object_or_404
from django.template.response import TemplateResponse

from django.http import HttpResponse
import django.core.exceptions

from . forms import CompetitionAddForm, Competition, HorseFormAdd, TeamAddForm
from . models import Competition, Team, CustomUser, Horse


def index(request):
    return TemplateResponse(request, "index.html", {})


def list_competition_view(request):
    competition = Competition.objects.all()
    return TemplateResponse(request, "list_competition_view.html", {'list_competition': competition})


def list_horses_view(request):
    horses = Horse.objects.all()
    return TemplateResponse(request, "list_horses_view.html", {'list_horses': horses})


def team_view(request, team_pk):
    pairs = get_object_or_404(Team, pk=team_pk).pairs.all()
    return TemplateResponse(request, "list_team_view.html", {'pairs': pairs})


def create_competition(request):
    if request.method == 'POST':
        f = CompetitionAddForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect(list_competition_view)
    elif request.method == 'GET':
        f = CompetitionAddForm()
    else:
        assert False
    return TemplateResponse(request, "create_competition.html", {
        "form": f
    })


def create_horse(request):
    if request.method == 'POST':
        f = HorseFormAdd(request.POST)
        if f.is_valid():
            f.save()
            return redirect(list_horses_view)
    elif request.method == 'GET':
        f = HorseFormAdd()
    else:
        assert False
    return TemplateResponse(request, "create_horse.html", {
        "form": f
    })


def create_team(request):
    if request.method == 'POST':
        f = TeamAddForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect(create_team)
    elif request.method == 'GET':
        f = TeamAddForm()
    else:
        assert False
    return TemplateResponse(request, "create_team.html", {
        "form": f
    })
