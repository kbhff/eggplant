#!/usr/bin/env python
import os
import sys

try:
    from foodnet_project.settings import local  # @UnusedImport
except ImportError:
    
    from foodnet_project import settings
    local_location = os.path.dirname(settings.__file__)
    open(
        os.path.join(local_location, 'local.py'),
        "w"
    ).write(
        open(os.path.join(local_location, 'local.py.sample')).read()
    )

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'foodnet_project.settings.local')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
