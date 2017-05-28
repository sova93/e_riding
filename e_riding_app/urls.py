from django.conf.urls import url
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    # main
    url(r'^$', views.MainPageView.as_view(), name='index'),
    # competition
    url(r'competition/new', views.CompetitionNewView.as_view(), name="competition-new"),
    url(r'competitions', views.CompetitionsView.as_view(), name="competitions"),
    url(r'competition/(?P<competition_pk>[\d]+)/edit', views.CompetitionEditView.as_view(), name="competition-edit"),
    url(r'competition/(?P<competition_pk>[\d]+)/map', views.CompetitionMapView.as_view(), name="competition-map"),
    url(r'competition/(?P<competition_pk>[\d]+)/api/points', views.get_competition_points, name="competition-api-points"),
    url(r'competition/(?P<competition_pk>[\d]+)', views.CompetitionView.as_view(), name="competition-pk"),
    # horse
    url(r'horse/new', views.HorseNewView.as_view(), name="horse-new"),
    url(r'horse/(?P<horse_pk>[\d]+)/update', views.HorseUpdateView.as_view(), name="horse-update"),
    url(r'horse/(?P<horse_pk>[\d]+)/delete', views.HorseDeleteView.as_view(), name="horse-delete"),
    url(r'horses', views.HorsesView.as_view(), name="horses"),
    # team
    url(r'team/new', views.TeamNewView.as_view(), name="team-new"),
    url(r'team/(?P<team_pk>[\d]+)', views.TeamView.as_view(), name="team-pk"),
    url(r'competition/(?P<competition_pk>[\d]+)/teams', views.TeamInCompetitionView.as_view(), name="teams-in-competition-pk"),
    # pair
    url(r'pair/new', views.PairNewView.as_view(), name="pair-new"),
    url(r'pairs', views.PairsView.as_view(), name="pairs"),
    # description step
    url(r'description_step/new', views.DescriptionStepNewViewMixin.as_view(), name="description-step-new"),
    # user
    url(r'user/new', views.UserNewView.as_view(), name="signup"),
    # pair on start
    url(r'pair_on_start/new', views.PairOnStartNewView.as_view(), name="pair-on-start-new"),
    # misc
    url(r'statistic_way', views.StatisicsWayView.as_view(), name="statistic_way"),
    url(r'login', views.AppLoginView.as_view(), name="login"),
    url(r'logout', views.AppLogoutView.as_view(), name="logout"),

    # ????????
    # url(r'update_horse_view/(?P<horse_pk>[\d]+)', views.update_horse_view, name="update_horse_view"),
    ]

if settings.DEBUG :
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]