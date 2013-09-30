from belvedere.apps.common.plugins import manager


def navigation(request):
    plugin_navigation = {}

    for plugin in manager.plugins.get_plugins():
        # plugin navigation
        plugin_nav = plugin.get_navigation()
        if plugin_nav:
            plugin_navigation[plugin.get_short()] = plugin_nav

    return {
        'navigation': plugin_navigation
    }
