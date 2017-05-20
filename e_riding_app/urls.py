from django.conf.urls import url
from . import views

urlpatterns = [
    # main
    url(r'^$', views.MainPageView.as_view(), name='index'),
    # competition
    url(r'competition/new', views.CompetitionNewView.as_view(), name="competition-new"),
    # url(r'competition/(?P<competition_pk>[\d]+)', views.competition_by_pk, name="competition-pk"),
    url(r'competitions', views.CompetitionsView.as_view(), name="competitions"),
    # horse
    url(r'horse/new', views.horse_new, name="horse-new"),
    # url(r'horse/(?P<horse_pk>)', views.horse_by_pk, name="horse-pk"),
    url(r'horse/(?P<horse_pk>[\d]+)/update', views.horse_update, name="horse-update"),
    url(r'horse/(?P<horse_pk>[\d]+)/delete', views.horse_delete, name="horse-delete"),
    url(r'horses', views.HorsesView.as_view(), name="horses"),
    # team
    url(r'team/new', views.team_new, name="team-new"),
    url(r'team/(?P<team_pk>[\d]+)', views.TeamView.as_view(), name="team-pk"),
    url(r'competition/(?P<competition_pk>[\d]+)/teams', views.TeamInCompetitionView.as_view(), name="teams-in-competition-pk"),
    # pair
    url(r'pair/new', views.pair_new, name="pair-new"),
    url(r'pairs', views.PairsView.as_view(), name="pairs"),
    # url(r'pair/(?P<pair_pk>[\d]+)', views.pair_by_pk, name="pair-pk"),
    # description step
    url(r'description_step/new', views.description_step_new, name="description-step-new"),
    # user
    url(r'user/new', views.user_new, name="user-new"),
    # pair on start
    url(r'pair_on_start/new', views.pair_on_start_new, name="pair-on-start-new"),
    # misc
    url(r'statistic_way', views.statistic_way, name="statistic_way"),
    url(r'auth', views.auth, name="auth"),
    # ????????
    # url(r'update_horse_view/(?P<horse_pk>[\d]+)', views.update_horse_view, name="update_horse_view"),
    ]

