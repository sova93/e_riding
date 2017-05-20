from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse_lazy
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views import generic
import django.core.exceptions

from . forms import CompetitionAddForm, PairAddForm, HorseAddForm, TeamAddForm, PairOnStartAddForm,\
    DescriptionStepAddForm, UserAddForm, UserAuthenticateForm
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


def auth(request):
    import warnings
    warnings.warn("function based view are deprecated!!!")
    if request.method == 'POST':
        f = UserAuthenticateForm(request.POST)
        print(f)
        if f.is_valid():
            print("ok")
            user = authenticate(f)
            print(user)
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    print("User is valid, active and authenticated")
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
            return redirect(index)
    elif request.method == 'GET':
        f = UserAuthenticateForm()
    else:
        assert False
    return TemplateResponse(request, "auth.html", {
        "form": f
    })


class HorseDeleteView(generic.DeleteView):
    form_class = UserAddForm
    success_url = reverse_lazy("horses")


class HorseUpdateView(_BaseViewMixin, generic.UpdateView):
    form_class = HorseAddForm
    template_name = "horse_update.html"


# def horse_update(request, horse_pk):
#     horse = get_object_or_404(Horse, pk=horse_pk)
#     f = HorseAddForm(instance=horse)
#     return TemplateResponse(request, "horse_update.html", {
#         "form": f, "horse_pk": horse_pk
#     })


# def update_horse_view(request, horse_pk):
#     instance = get_object_or_404(Horse, pk=horse_pk)
#     f = HorseAddForm(request.POST or None, instance=instance)
#     if f.is_valid():
#         f.save()
#         return redirect(horses)
#     else:
#         assert False

class StatisicsWayView(generic.TemplateView):
    template_name = "statistic_way.html"
