# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False, editable=False, default=uuid.uuid4)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=15, choices=[('open', 'open'), ('checked-out', 'checked-out')], default='open')),
                ('order', models.OneToOneField(null=True, to='payments.Order')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('basket', models.ForeignKey(to='webshop.Basket', related_name='items')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('category', models.CharField(null=True, max_length=50, choices=[('weekly bag', 'weekly bag'), ('dry goods', 'dry goods'), ('loose weight vegetables', 'loose weight vegetables'), ('dairy', 'dairy'), ('fee', 'fee')])),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, default=0)),
                ('stock', models.PositiveIntegerField(default=1)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=5, default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('image', models.ImageField(null=True, upload_to='products')),
            ],
        ),
        migrations.AddField(
            model_name='basketitem',
            name='product',
            field=models.ForeignKey(to='webshop.Product'),
        ),
        migrations.AlterUniqueTogether(
            name='basketitem',
            unique_together=set([('basket', 'product')]),
        ),
        migrations.AlterIndexTogether(
            name='basket',
            index_together=set([('user', 'status')]),
        ),
    ]
