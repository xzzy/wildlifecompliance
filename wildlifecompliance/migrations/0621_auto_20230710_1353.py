# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-07-10 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0620_masterlistquestion_help_text_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterlistquestion',
            name='help_text_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
