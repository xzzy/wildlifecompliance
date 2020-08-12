# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-05-09 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0192_auto_20190509_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporttype',
            name='advice_details',
        ),
        migrations.RemoveField(
            model_name='reporttype',
            name='advice_given',
        ),
        migrations.RemoveField(
            model_name='reporttype',
            name='referrer',
        ),
        migrations.AddField(
            model_name='callemail',
            name='advice_details',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='callemail',
            name='advice_given',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='callemail',
            name='referrer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_referrer', to='wildlifecompliance.Referrer'),
        ),
    ]