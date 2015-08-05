from __future__ import unicode_literals
from django.db import models, migrations


def add_default_fees(apps, schema_editor):
    #FeeConfig = apps.get_model("payments", "FeeConfig")
    from eggplant.payments.models import FeeConfig
    FeeConfig.objects.create(
        name='membership',
        amount=10.00,
        application=FeeConfig.MONTHLY,
        currency='DKK',
    )
    FeeConfig.objects.create(
        name='sign-up',
        amount=15.00,
        application=FeeConfig.ONE_OFF,
        currency='DKK',
    )

class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_fees),
    ]
