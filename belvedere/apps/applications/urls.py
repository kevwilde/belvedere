from . import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^hi$', views.ApplicationSummary.as_view(), name='appl-summary'),
)
