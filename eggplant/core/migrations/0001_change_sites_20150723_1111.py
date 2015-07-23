#  coding: utf-8
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


def change_sites(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    Site.objects.filter(domain='example.com').delete()
    Site.objects.get_or_create(id=settings.SITE_ID, domain=settings.DOMAIN)


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial')
    ]

    operations = [
        migrations.RunPython(change_sites,
                             reverse_code=migrations.RunPython.noop),
    ]
