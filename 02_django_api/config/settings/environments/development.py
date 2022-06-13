"""
This file contains all the settings that defines the development server.
SECURITY WARNING: don't run with debug turned on in production!
"""

import socket

from config.settings.components import config
from config.settings.components.common import INSTALLED_APPS, MIDDLEWARE

# Setting the development status:
DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS_DEV', '').split(' ')

# Installed apps for development only:
INSTALLED_APPS += [
    'debug_toolbar',
]

# Django debug toolbar:
# https://django-debug-toolbar.readthedocs.io
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

# https://django-debug-toolbar.readthedocs.io/en/stable/installation.html#configure-internal-ips
INTERNAL_IPS = [
                   '{0}.1'.format(ip[:ip.rfind('.')])
                   for ip in socket.gethostbyname_ex(socket.gethostname())[2]
               ] + ['127.0.0.1', '10.0.2.2', '192.168.0.10']


def _custom_show_toolbar(request):
    """Only show the debug toolbar to users with the superuser flag."""
    return DEBUG and request.user.is_superuser and request.META['REMOTE_ADDR'] in INTERNAL_IPS


DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': _custom_show_toolbar}

SECURE_CROSS_ORIGIN_OPENER_POLICY = None
