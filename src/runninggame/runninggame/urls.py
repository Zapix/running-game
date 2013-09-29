from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('simplegame.urls')),
    url(r'^', include('websocket.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('userprofile.urls'))
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
