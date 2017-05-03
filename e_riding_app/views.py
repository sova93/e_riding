from django.shortcuts import render, redirect, get_object_or_404
from django.template.response import TemplateResponse

from django.http import HttpResponse
import django.core.exceptions

from . forms import CompetitionAddForm, PairAddForm, HorseAddForm, TeamAddForm, PairOnStartAddForm,\
    DescriptionStepAddForm
from . models import Competition, Team, CustomUser, Horse, Pair, PairOnStart


def index(request):
    return TemplateResponse(request, "index.html", {})


def list_competition_view(request):
    competition = Competition.objects.all()
    return TemplateResponse(request, "list_competition_view.html", {'list_competition': competition})


def list_horses_view(request):
    horses = Horse.objects.all()
    return TemplateResponse(request, "list_horses_view.html", {'list_horses': horses})


def list_pairs_all(request):
    pairs = Pair.objects.all()
    return TemplateResponse(request, "list_pairs_all.html", {'pairs': pairs})


def list_team_view(request, team_pk):
    team = get_object_or_404(Team, pk=team_pk)
    pairs = get_object_or_404(Team, pk=team_pk).pairs.all()
    return TemplateResponse(request, "list_team_view.html", {'pairs': pairs, 'team': team})


def list_teams_view_on_competition(request, competition_pk):
    competition = get_object_or_404(Competition, pk=competition_pk)
    teams = get_object_or_404(Competition, pk=competition_pk).teams.all()
    return TemplateResponse(request, "list_teams_view_on_competition.html", {'teams': teams, 'competition': competition})


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


def create_description_step(request):
    if request.method == 'POST':
        f = DescriptionStepAddForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect(create_description_step)
    elif request.method == 'GET':
        f = DescriptionStepAddForm
    else:
        assert False
    return TemplateResponse(request, "create_description_step.html", {
        "form": f
    })


def create_horse(request):
    if request.method == 'POST':
        f = HorseAddForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect(list_horses_view)
    elif request.method == 'GET':
        f = HorseAddForm()
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


def create_pair(request):
    print('DONT OK')
    if request.method == 'POST':
        f = PairAddForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect(create_pair)
    elif request.method == 'GET':
        f = PairAddForm()
    else:
        assert False
    return TemplateResponse(request, "create_pair.html", {
        "form": f
    })


def create_pair_on_start(request):
    print('OK')
    if request.method == 'POST':
        f = PairOnStartAddForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect(create_pair_on_start)
    elif request.method == 'GET':
        f = PairOnStartAddForm()
    else:
        assert False
    return TemplateResponse(request, "create_pair_on_start.html", {
        "form": f
    })


def delete_horse(request, horse_pk):
    horse = get_object_or_404(Horse, pk=horse_pk)
    horse.delete()
    return redirect("list_horses_view")


def update_horse(request, horse_pk):
    horse = get_object_or_404(Horse, pk=horse_pk)
    f = HorseAddForm(instance=horse)
    return TemplateResponse(request, "update_horse.html", {
        "form": f, "horse_pk": horse_pk
    })


def update_horse_view(request, horse_pk):
    instance = get_object_or_404(Horse, pk=horse_pk)
    print(instance)
    f = HorseAddForm(request.POST or None, instance=instance)
    if f.is_valid():
        f.save()
        return redirect(list_horses_view)
    else:
        assert False