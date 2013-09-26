class WidgetManager(object):

    _widgets = []

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(WidgetManager, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print "Initialized WidgetManager"
        print "Widgets: %s" % self._widgets

    def register(self, widget_name, widget_cls):
        instance = widget_cls()
        instance.short = widget_name
        print "Registered widget '%s'" % instance.title
        self._widgets.append(instance)

    def get_widgets(self):
        print "Returning widgets"
        return self._widgets
