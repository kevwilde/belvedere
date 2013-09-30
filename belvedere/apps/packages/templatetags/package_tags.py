import requests

from django import template

register = template.Library()


class PackageInfoNode(template.Node):

    def __init__(self, hostname, package):
        self.hostname = hostname
        self.package = package
        # variable lookup
        self.hostname = template.Variable(hostname)
        self.package = template.Variable(package)


    def render(self, context):
        try:
            hostname = self.hostname.resolve(context)
            package = self.package.resolve(context)
            # query the host for the package
            pkg_info = requests.get(
                'http://%s/_scenic/pkg/%s' % (hostname, package),
                timeout=1).json()
            return pkg_info
        except ValueError:
            return "Unknown"
        except template.VariableDoesNotExist:
            return "Unknown"


def package_info(parser, token):
    try:
        tag_name, hostname, package = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires a two arguments" % token.contents.split()[0])
    return PackageInfoNode(hostname, package)


@register.filter(name='package_info')
def package_info(server, package):
    try:
        pkg_info = requests.get(
            'http://%s/_scenic/pkg/%s' % (server.hostname, package),
            timeout=1).json()
    except:
        try:
            pkg_info = requests.get(
            'http://%s/ajax/local/%s' % (server.hostname, package),
            timeout=1).json()
        except:
            return "Unknown"
    return pkg_info

#register.tag('package_info', package_info)

