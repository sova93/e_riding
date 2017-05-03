from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create_competition', views.create_competition, name="create_competition"),
    url(r'create_horse', views.create_horse, name="create_horse"),
    url(r'create_team', views.create_team, name="create_team"),
    url(r'create_pair_on_start', views.create_pair_on_start, name="create_pair_on_start"),
    url(r'create_pair', views.create_pair, name="create_pair"),
    url(r'create_description_step', views.create_description_step, name="create_description_step"),
    url(r'list_competition_view', views.list_competition_view, name="list_competition_view"),
    url(r'list_horses_view', views.list_horses_view, name="list_horses_view"),
    url(r'list_pairs_all', views.list_pairs_all, name="list_pairs_all"),
    url(r'list_horses/(?P<horse_pk>[\d]+)/delete', views.delete_horse, name="delete_horse"),
    url(r'list_horses/(?P<horse_pk>[\d]+)/update', views.update_horse, name="update_horse"),
    url(r'list_teams_view_on_competition/(?P<competition_pk>[\d]+)', views.list_teams_view_on_competition, name="list_teams_view_on_competition"),
    url(r'update_horse_view/(?P<horse_pk>[\d]+)', views.update_horse_view, name="update_horse_view"),
    url(r'team/(?P<team_pk>[\d]+)', views.list_team_view, name="list_team_view"),
]
