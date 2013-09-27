from django.views.generic.list import ListView
from .models import Application


class ApplicationSummary(ListView):
    template_name = "applications/summary.html"
    model = Application
