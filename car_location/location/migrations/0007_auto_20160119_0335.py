# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20160119_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucao',
            name='locacao',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='location.Locacao', verbose_name='locação'),
        ),
    ]
