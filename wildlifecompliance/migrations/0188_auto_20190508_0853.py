# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-05-08 00:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0187_callemail_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callemail',
            name='schema',
        ),
        migrations.AlterField(
            model_name='callemail',
            name='report_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='call_schema', to='wildlifecompliance.ReportType'),
        ),
    ]