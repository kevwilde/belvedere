from django.conf.urls import patterns
from django.template import loader


class PluginDefinition(object):

    _short = None
    _widgets = []
    _urlpattern = None

    def add_widget(self, widget_cls):
        inst = widget_cls()
        self._widgets.append(inst)

    def get_widgets(self):
        return self._widgets

    def add_urlpattern(self, urlpattern):
        self._urlpattern = urlpattern

    def get_urlpatterns(self):
        if self._urlpattern:
            return self._urlpattern
        else:
            return patterns()

    def get_short(self):
        return self._short

class Widget(object):
    title = None
    widget_template = None

    def get_context_data(self, **kwargs):
        """
        Returns a context dictionary to be used when rendering
        the widget.
        """
        return kwargs

    def get_widget_template(self):
        if self.widget_template:
            return self.widget_template
        else:
            return "widgets/%s.html" % self.__class__.__name__.lower()

    def _render_widget_body(self):
        context = self.get_context_data()
        return loader.render_to_string(
            self.get_widget_template(), context
        )

    def render(self):
        context = {
            'widget_body': self._render_widget_body(),
            'widget_title': self.title
        }
        return loader.render_to_string(
            "widget_container.html", context
        )
