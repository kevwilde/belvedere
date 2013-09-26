from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from apps.common import views

admin.autodiscover()



urlpatterns = patterns('',

    url(r'^$', views.WidgetOverview.as_view(), name='home'),
    #url(r'^applications/', include('apps.applications.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin
    url(r'^admin/', include(admin.site.urls)),

)

#if settings.DEBUG:
urlpatterns += staticfiles_urlpatterns()
