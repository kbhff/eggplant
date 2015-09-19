# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('open', 'open'), ('checked-out', 'checked-out')], default='open', max_length=15)),
                ('user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('basket', models.ForeignKey(related_name='items', to='webshop.Basket')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=512)),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.DecimalField(default=0, max_digits=12, verbose_name='title', help_text='Price of product without VAT and taxes.', decimal_places=2)),
                ('stock', models.PositiveIntegerField(default=1, null=True, verbose_name='stock', help_text='Items in stock, leave blank if endless quantity available.')),
                ('enabled', models.BooleanField(verbose_name='enabled', default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('enabled', models.BooleanField(verbose_name='enabled', default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTax',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=512)),
                ('description', models.TextField(verbose_name='description')),
                ('enabled', models.BooleanField(verbose_name='enabled', default=True)),
                ('tax', models.DecimalField(verbose_name='tax', max_digits=5, help_text="A factor, e.g. '0.25' adds 25% to value in order.", decimal_places=4)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='webshop.ProductCategory', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.ForeignKey(to='webshop.ProductTax', verbose_name='tax'),
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
