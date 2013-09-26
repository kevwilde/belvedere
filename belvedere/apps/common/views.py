from django.views.generic.base import TemplateView

class WidgetOverview(TemplateView):

    template_name = "overview.html"

    def get_context_data(self, **kwargs):
        from .widgetmanager import manager
        context = super(WidgetOverview, self).get_context_data(**kwargs)
        context['widgets'] = manager.widgets.get_widgets()
        return context
