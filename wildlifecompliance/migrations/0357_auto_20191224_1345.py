# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-12-24 05:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0356_remediationactiontaken_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionTakenDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('uploaded_date', models.DateTimeField(auto_now_add=True)),
                ('_file', models.FileField(max_length=255, upload_to=b'')),
            ],
            options={
                'verbose_name': 'CM_RemediationActionDocument',
                'verbose_name_plural': 'CM_RemediationActionDocuments',
            },
        ),
        migrations.AddField(
            model_name='remediationaction',
            name='action_taken',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='actiontakendocument',
            name='remediation_action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='wildlifecompliance.RemediationAction'),
        ),
    ]