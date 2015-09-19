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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('open', 'open'), ('checked-out', 'checked-out')], max_length=15, default='open')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('basket', models.ForeignKey(to='webshop.Basket', related_name='items')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('amount', models.DecimalField(decimal_places=2, verbose_name='amount to be paid', max_digits=12)),
                ('currency', models.CharField(choices=[('DKK', 'DKK'), ('PLN', 'PLN'), ('GBP', 'GBP')], max_length=3, default='DKK')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=512, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.DecimalField(default=0, decimal_places=2, max_digits=12, verbose_name='title', help_text='Price of product without VAT and taxes.')),
                ('stock', models.PositiveIntegerField(null=True, default=1, verbose_name='stock', help_text='Items in stock, leave blank if endless quantity available.')),
                ('enabled', models.BooleanField(verbose_name='enabled', default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('enabled', models.BooleanField(verbose_name='enabled', default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTax',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=512, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('enabled', models.BooleanField(verbose_name='enabled', default=True)),
                ('tax', models.DecimalField(decimal_places=4, max_digits=5, verbose_name='tax', help_text="A factor, e.g. '0.25' adds 25% to value in order.")),
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
