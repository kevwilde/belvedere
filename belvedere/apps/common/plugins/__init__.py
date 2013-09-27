import sys

from django.utils.importlib import import_module
from apps.common.plugins import manager


def autodiscover(module_name):
    """
    Dynamically autodiscover a
    particular module_name in a django project's INSTALLED_APPS directories,
    a-la django admin's autodiscover() method.

    Usage:
        autodiscover('commands') <-- find all commands.py and load 'em
    """
    import imp
    from django.conf import settings

    for app in settings.INSTALLED_APPS:
        if u"django.contrib" in app:
            continue
        try:
            import_module(app)
            app_path = sys.modules[app].__path__
        except AttributeError:
            continue
        try:
            imp.find_module(module_name, app_path)
        except ImportError:
            continue
        print "Importing %s.%s" % (app, module_name)
        import_module('%s.%s' % (app, module_name))
        app_path = sys.modules['%s.%s' % (app, module_name)]


# Autodiscover all plugins
manager.plugins = manager.PluginManager()
autodiscover('plugin')
