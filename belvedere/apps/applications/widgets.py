from apps.common.plugins.models import Widget

from .models import Application


class ApplicationListWidget(Widget):
    title = "Applications"
    widget_template = "applications/widgets/applist.html"

    def get_context_data(self, **kwargs):
        context = super(ApplicationListWidget, self).get_context_data(**kwargs)
        context['applications'] = Application.objects.all()
        return context
