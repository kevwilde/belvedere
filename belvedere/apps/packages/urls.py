from . import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', views.InstalledPackagesOverview.as_view(), name='pkgs-installed'),
)
