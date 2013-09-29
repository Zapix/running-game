# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from . import views

urlpatterns = patterns(
    '',
    url(r'^signup/$', views.RegistrationFormView.as_view(), name='signup'),
    url(r'^finished/$', views.RegistrationFinished.as_view(),
        name='registration_finished'),
    url(r'^profile/$', views.AccountRedirectView.as_view(), name='profile'),
    url(r'^profile/(?P<pk>\d+)', views.AccountProfileView.as_view(),
        name='account_profile')
)
