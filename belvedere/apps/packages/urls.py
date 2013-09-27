from . import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', views.InfrastructureOverview.as_view(), name='infra-overview'),
)
