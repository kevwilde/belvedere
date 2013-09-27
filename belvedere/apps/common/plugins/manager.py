class PluginManager(object):

    _plugins = dict()

    def __init__(self):
        print "Initialized PluginManager"
        print "Plugins: %s" % self._plugins

    def register(self, plugin_name, plugin_cls):
        instance = plugin_cls()
        instance._short = plugin_name
        print "Registered widget '%s'" % instance._short
        self._plugins[plugin_name] = instance

    def get_plugins(self):
        print "Returning widgets"
        return self._plugins.itervalues()
