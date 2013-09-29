from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views import generic as cbv

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', cbv.TemplateView.as_view(template_name='home.html'),
        name='home'),
    url(r'^about/$', cbv.TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('websocket.urls')),

    url(r'^game/', include('simplegame.urls')),

    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('userprofile.urls'))
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
