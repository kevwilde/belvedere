from django.views.generic.list import ListView
from apps.packages.models import SystemPackage


class InfrastructureOverview(ListView):
    template_name = "infrastructure/overview.html"
    model = SystemPackage
