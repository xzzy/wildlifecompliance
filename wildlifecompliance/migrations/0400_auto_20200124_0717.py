# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-01-23 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0399_auto_20200122_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='briefofevidencerecordofinterview',
            name='offender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='offender_boe_roi', to='wildlifecompliance.Offender'),
        ),
    ]