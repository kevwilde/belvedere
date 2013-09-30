from django.views.generic.list import ListView
from apps.applications.models import Application

from apps.infrastructure.models import Server
from apps.packages.models import SystemPackage


class InstalledPackagesOverview(ListView):
    template_name = "packages/overview.html"
    #model = Server

    def get_queryset(self):
        return Server.objects.all().order_by('environment', 'hostname')

    def get_context_data(self, **kwargs):
        context = super(InstalledPackagesOverview, self).get_context_data(**kwargs)
        context['package_list'] = SystemPackage.objects.all()
        context['application_list'] = Application.objects.all()
        return context
