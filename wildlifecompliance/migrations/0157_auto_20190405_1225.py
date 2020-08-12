# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-04-05 04:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0156_merge_20190404_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=10)),
                ('street', models.CharField(max_length=100)),
                ('town_suburb', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('WA', 'Western Australia'), ('VIC', 'Victoria'), ('QLD', 'Queensland'), ('NSW', 'New South Wales'), ('TAS', 'Tasmania'), ('NT', 'Northern Territory'), ('ACT', 'Australian Capital Territory')], default='WA', max_length=50)),
                ('postcode', models.IntegerField()),
                ('country', models.CharField(default='Australia', max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='callemail',
            name='anonymous_call',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='callemail',
            name='caller_wishes_to_remain_anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='applicationselectedactivity',
            name='processing_status',
            field=models.CharField(choices=[('draft', 'Draft'), ('with_officer', 'With Officer'), ('with_assessor', 'With Assessor'), ('with_officer_conditions', 'With Officer-Conditions'), ('with_officer_finalisation', 'With Officer-Finalisation'), ('accepted', 'Accepted'), ('declined', 'Declined'), ('discarded', 'Discarded')], default='draft', max_length=30, verbose_name='Processing Status'),
        ),
        migrations.AddField(
            model_name='callemail',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='wildlifecompliance.Location'),
        ),
    ]