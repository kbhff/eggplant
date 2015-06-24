#!/usr/bin/env python
import os
import sys

try:
    from eggplant_project.settings import local  # @UnusedImport
except ImportError:
    
    from eggplant_project import settings
    local_location = os.path.join(
        os.path.dirname(settings.__file__),
        'local.py'
    )
    if not os.path.isfile(local_location):
        open(
            local_location,
            "w"
        ).write(
            open(os.path.join(local_location, 'local.py.sample')).read()
        )

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'eggplant_project.settings.local')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
