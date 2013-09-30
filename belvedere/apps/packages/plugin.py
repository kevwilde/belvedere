"""
Definition of the application plugin.

Belvedere will search after plugin modules in each installed application.
If a plugin module is found, the application will be considered a plugin
by Belvedere. It will then try to register it as a plugin, searching for
widgets and urlpatterns.

"""
from .urls import urlpatterns

from apps.common.plugins import manager
from apps.common.plugins.models import PluginDefinition


class PackagesPlugin(PluginDefinition):

    def __init__(self):
        super(PackagesPlugin, self).__init__()
        # Add urlpattern
        self.add_urlpattern(urlpatterns)

# Register plugin
manager.plugins.register('packages', PackagesPlugin)
