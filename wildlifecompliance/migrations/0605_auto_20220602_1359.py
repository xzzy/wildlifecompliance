# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-02 05:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wildlifecompliance', '0604_auto_20220601_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComplianceAdminGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CM Compliance Admin Group',
                'verbose_name_plural': 'CM Compliance Admin Groups',
            },
        ),
        migrations.CreateModel(
            name='ComplianceManagementApprovedExternalUserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CM Compliance Management Approved External User Group',
                'verbose_name_plural': 'CM Compliance Management Approved External User Groups',
            },
        ),
        migrations.CreateModel(
            name='ComplianceManagementCallEmailReadOnlyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CM Compliance Management Call Email Read Only Group',
                'verbose_name_plural': 'CM Compliance Management Call Email Read Only Groups',
            },
        ),
        migrations.CreateModel(
            name='ComplianceManagementReadOnlyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CM Compliance Management Read Only Group',
                'verbose_name_plural': 'CM Compliance Management Read Only Groups',
            },
        ),
        migrations.CreateModel(
            name='InfringementNoticeCoordinatorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CM_InfringementNoticeCoordinatorGroup',
                'verbose_name_plural': 'CM Infringement Notice Coordinator Groups',
            },
        ),
        migrations.CreateModel(
            name='LicensingAdminGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CM Licensing Admin Group',
                'verbose_name_plural': 'CM Licensing Admin Groups',
            },
        ),
        migrations.CreateModel(
            name='ProsecutionCoordinatorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CM_ProsecutionCoordinatorGroup',
                'verbose_name_plural': 'CM Prosecution Coordinator Groups',
            },
        ),
        migrations.CreateModel(
            name='ProsecutionCouncilGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CM Prosecution Council Group',
                'verbose_name_plural': 'CM Prosecution Council Groups',
            },
        ),
        migrations.CreateModel(
            name='ProsecutionManagerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'CM Prosecution Manager Group',
                'verbose_name_plural': 'CM Prosecution Manager Groups',
            },
        ),
        migrations.AlterModelOptions(
            name='callemailtriagegroup',
            options={'verbose_name': 'CM_CallEmailTriageGroup', 'verbose_name_plural': 'CM CallEmail Triage Groups'},
        ),
        migrations.AlterModelOptions(
            name='managergroup',
            options={'verbose_name': 'CM_ManagerGroup', 'verbose_name_plural': 'CM Manager_Groups'},
        ),
        migrations.AlterModelOptions(
            name='officergroup',
            options={'verbose_name': 'CM_OfficerGroup', 'verbose_name_plural': 'CM Officer Groups'},
        ),
        migrations.AlterModelOptions(
            name='volunteergroup',
            options={'verbose_name': 'CM_Volunteer', 'verbose_name_plural': 'CM Volunteers'},
        ),
    ]