from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'create_competition', views.create_competition, name="create_competition"),
    url(r'list_competition_view', views.list_competition_view, name="list_competition_view"),

    url(r'create_horse', views.create_horse, name="create_horse"),
    url(r'list_horses_view', views.list_horses_view, name="list_horses_view"),

    url(r'create_team', views.create_team, name="create_team"),
    # url(r'list_team_view', views.list_team_view, name="list_team_view"),

    url(r'team/(?P<team_pk>[\d]+)', views.team_view, name="team_view"),
]
