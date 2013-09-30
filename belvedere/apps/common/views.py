from django.views.generic.base import TemplateView
from apps.common.plugins import manager


class WidgetOverview(TemplateView):

    template_name = "overview.html"

    def get_context_data(self, **kwargs):
        context = super(WidgetOverview, self).get_context_data(**kwargs)
        widgets = []

        for plugin in manager.plugins.get_plugins():
            # plugin widgets
            widgets += plugin.get_widgets()
        context['widgets'] = widgets

        return context
