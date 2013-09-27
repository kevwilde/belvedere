import os
import re


def local_package_information(package):
    # read package control file
    pkg_control = os.popen('dpkg -s %s' % package).read()

    # parse the control information just enough
    version = re.search('Version: (.*?)\n', pkg_control)
    if version:
        version = version.group(1)

    # prepare package information
    pkg_info = {
        'name': package,
        'version': version,
        'controlfile': pkg_control
    }
    return pkg_info
