from apps.common.widgetmanager import manager
from apps.common.widgetmanager.widget import Widget

from .models import Application


class ApplicationListWidget(Widget):
    title = "Application List"

    def get_context_data(self, **kwargs):
        context = super(ApplicationListWidget, self).get_context_data(**kwargs)
        context['applications'] = Application.objects.all()
        return context

manager.widgets.register('applist', ApplicationListWidget)
