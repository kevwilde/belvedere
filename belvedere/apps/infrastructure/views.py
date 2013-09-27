from django.views.generic.list import ListView
from apps.infrastructure.models import Deployment


class InfrastructureOverview(ListView):
    template_name = "infrastructure/overview.html"
    model = Deployment
