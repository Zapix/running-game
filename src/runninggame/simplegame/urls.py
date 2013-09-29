# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexGameView.as_view(), name='index_game'),
    url(r'^pad/(?P<auth_code>\d+)/$', views.GamePadView.as_view(),
        name='gamepad'),
    url(r'^played/game/list/$', views.PlayedGameListView.as_view(),
        name='played_game_list')
)
