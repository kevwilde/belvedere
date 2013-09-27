from . import views
from django.conf.urls import patterns, url

urlpatterns = patterns('',

    url(r'^pkg/(?P<pkgname>\w+)/',
        views.PackageDetailView.as_view(),
        name='scenic-package-details')

)
