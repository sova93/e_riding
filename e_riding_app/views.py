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
    objs = [
        {
            "user": "user1",
            "lon": 27.124080061912537,
            "lat": 53.8032803552915,
        },
        {
            "user": "user2",
            "lon": 27.113828659057617,
            "lat": 53.81230820557223,
        },
        {
            "user": "user3",
            "lon": 27.10275650024414,
            "lat": 53.819731759517694,
        },
        {
            "user": "user4",
            "lon": 27.089452743530273,
            "lat": 53.82044110880845,
        },
        {
            "user": "user5",
            "lon": 27.090697288513184,
            "lat": 53.820491776155436,
        },
        {
            "user": "user6",
            "lon": 27.080097198486328,
            "lat": 53.81894639451032,
        },
        {
            "user": "user7",
            "lon": 27.066707611083984,
            "lat": 53.81955442031875,
        },
        {
            "user": "user8",
            "lon": 27.048640251159668,
            "lat": 53.81980776180178,
        },
        {
            "user": "user9",
            "lon": 27.01662540435791,
            "lat": 53.823455709331334,
        },
        {
            "user": "user10",
            "lon": 27.014265060424805,
            "lat": 53.822721078771124,
        },
        {
            "user": "user11",
            "lon": 27.010531425476074,
            "lat": 53.82310106170353,
        },
        {
            "user": "user12",
            "lon": 27.00417995452881,
            "lat": 53.82132777853571,
        },
        {
            "user": "user13",
            "lon": 27.00512409210205,
            "lat": 53.819225074101,
        },
        {
            "user": "user14",
            "lon": 27.01113224029541,
            "lat": 53.81415788296499,
        },
        {
            "user": "user15",
            "lon": 27.01310634613037,
            "lat": 53.80805110367027,
        },
        {
            "user": "user16",
            "lon": 27.017097473144528,
            "lat": 53.801842055061144,
        },
        {
            "user": "user17",
            "lon": 27.07855224609375,
            "lat": 53.79535325043358,
        },
        {
            "user": "user18",
            "lon": 27.091341018676754,
            "lat": 53.79654462965297,
        },
        {
            "user": "user19",
            "lon": 27.118420600891113,
            "lat": 53.80305859415585,
        },
        {
            "user": "user20",
            "lon": 27.11000919342041,
            "lat": 53.803413411409885,
        }]
    return HttpResponse(json.dumps(objs), content_type="application/json")


class StatisicsWayView(generic.TemplateView):
    template_name = "statistic_way.html"
