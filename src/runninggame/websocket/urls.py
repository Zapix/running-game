# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url('^socket\.io', views.socketio, name='socketio'),
)
