from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse_lazy
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views import generic
import django.core.exceptions

import json

from . forms import CompetitionAddForm, PairAddForm, HorseAddForm, TeamAddForm, PairOnStartAddForm,\
    DescriptionStepAddForm, UserAddForm
from . models import Competition, Team, CustomUser, Horse, Pair, PairOnStart


class _BaseViewMixin(object):
    context_object_name = "form"
    success_url = reverse_lazy("competitions")


class MainPageView(generic.TemplateView):
    template_name = "index.html"


class CompetitionsView(generic.ListView):
    model = Competition
    context_object_name = "competitions"
    template_name = "competitions.html"


class HorsesView(generic.ListView):
    model = Horse
    context_object_name = "horses"
    template_name = "horses.html"


class PairsView(generic.ListView):
    model = Pair
    context_object_name = "pairs"
    template_name = "pairs.html"


class TeamView(generic.TemplateView):
    template_name = "teams.html"

    def get_context_data(self, team_pk, **kwargs):
        ctx = super().get_context_data(team_pk=team_pk, **kwargs)
        ctx["team"] = get_object_or_404(Team, pk=team_pk)
        ctx["pairs"] = ctx["team"].pairs.all()
        return ctx


class TeamInCompetitionView(generic.TemplateView):
    template_name = "team_in_competition.html"

    def get_context_data(self, competition_pk, **kwargs):
        ctx = super().get_context_data(competition_pk=competition_pk, **kwargs)
        ctx["competition"] = get_object_or_404(Competition, pk=competition_pk)
        ctx["teams"] = ctx["competition"].teams.all()
        return ctx


class CompetitionNewView(_BaseViewMixin, generic.CreateView):
    form_class = CompetitionAddForm
    template_name = "competition-new.html"


class DescriptionStepNewViewMixin(_BaseViewMixin, generic.CreateView):
    form_class = DescriptionStepAddForm
    template_name = "description_step_new.html"


class HorseNewView(_BaseViewMixin, generic.CreateView):
    form_class = HorseAddForm
    template_name = "horse_new.html"


class TeamNewView(_BaseViewMixin, generic.CreateView):
    form_class = TeamAddForm
    template_name = "team_new.html"


class PairNewView(_BaseViewMixin, generic.CreateView):
    form_class = PairAddForm
    template_name = "pair_new.html"


class PairOnStartNewView(generic.CreateView):
    form_class = PairOnStartAddForm
    template_name = "pair_on_start_new.html"
    context_object_name = "form"
    success_url = reverse_lazy("competitions")


class UserNewView(_BaseViewMixin, generic.CreateView):
    form_class = UserAddForm
    template_name = "user_new.html"


class AppLoginView(LoginView):
    template_name = "auth.html"
    redirect_authenticated_user = True


class AppLogoutView(LogoutView):
    next_page = reverse_lazy("index")


class HorseDeleteView(generic.DeleteView):
    form_class = UserAddForm
    success_url = reverse_lazy("horses")


class HorseUpdateView(_BaseViewMixin, generic.UpdateView):
    form_class = HorseAddForm
    template_name = "horse_update.html"


class CompetitionMapView(_BaseViewMixin, generic.TemplateView):
    template_name = "competition/map.html"

    def get_context_data(self, competition_pk, **kwargs):
        ctx = super().get_context_data(competition_pk=competition_pk, **kwargs)
        ctx["competition"] = Competition.objects.get(pk=competition_pk)

        return ctx


def get_competition_points(request, competition_pk):
    objs = [{
        "user": "admin",
        "lat": 53.896944,
        "lon": 27.286226,
    },{
        "user": "vet",
        "lat": 53.895829,
        "lon":  27.295496,
    },{
        "user": "vet2",
        "lat": 53.888427,
        "lon":  27.296698,
    },{
        "user": "vet3",
        "lat": 53.890759,
        "lon":  27.281076,
    }]
    return HttpResponse(json.dumps(objs), content_type="application/json")


class StatisicsWayView(generic.TemplateView):
    template_name = "statistic_way.html"
