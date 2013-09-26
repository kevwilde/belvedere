from django.template import loader


class Widget(object):
    title = None
    short = None

    def get_context_data(self, **kwargs):
        """
        Returns a context dictionary to be used when rendering
        the widget.
        """
        return kwargs

    def get_widget_template(self):
        return "widgets/%s.html" % self.short

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
