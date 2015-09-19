# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=15, default='open', choices=[('open', 'open'), ('checked-out', 'checked-out')])),
                ('user', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('basket', models.ForeignKey(to='market.Basket', related_name='items')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('amount', models.DecimalField(max_digits=12, decimal_places=2, verbose_name='amount to be paid')),
                ('currency', models.CharField(max_length=3, default='DKK', choices=[('DKK', 'DKK'), ('PLN', 'PLN'), ('GBP', 'GBP')])),
                ('created', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=512, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('price', models.DecimalField(max_digits=12, decimal_places=2, help_text='Price of product without VAT and taxes.', default=0, verbose_name='title')),
                ('stock', models.PositiveIntegerField(null=True, help_text='Items in stock, leave blank if endless quantity available.', default=1, verbose_name='stock')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTax',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=512, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled')),
                ('tax', models.DecimalField(max_digits=5, help_text="A factor, e.g. '0.25' adds 25% to value in order.", decimal_places=4, verbose_name='tax')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='market.ProductCategory', verbose_name='category'),
        ),
        migrations.AddField(
            model_name='product',
            name='tax',
            field=models.ForeignKey(to='market.ProductTax', verbose_name='tax'),
        ),
        migrations.AddField(
            model_name='basketitem',
            name='product',
            field=models.ForeignKey(to='market.Product'),
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
