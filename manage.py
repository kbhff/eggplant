#!/usr/bin/env python
import os
import sys

try:
    from eggplant_settings import local  # @UnusedImport
except ImportError:

    import eggplant_settings as settings
    local_location = os.path.join(
        os.path.dirname(settings.__file__),
        'local.py'
    )
    local_sample_location = os.path.join(
        os.path.dirname(settings.__file__),
        'local.py.sample'
    )
    if not os.path.isfile(local_location):
        open(
            local_location,
            "w"
        ).write(open(local_sample_location).read())

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'eggplant_settings.local')

    os.environ.setdefault('LANG', 'en_US.utf8')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
