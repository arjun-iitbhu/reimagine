# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('audit_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('report_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('cause_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('consultant_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('ngo_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('person_of_contact', models.CharField(max_length=100)),
                ('registration_code', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('website', models.URLField()),
                ('team_member_id', models.ForeignKey(on_delete=models.SET('team member not set'), to='staff.Team_Member')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('raised_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('zip', models.IntegerField(blank=True)),
                ('person_of_contact', models.CharField(max_length=100)),
                ('summary', models.CharField(max_length=500)),
                ('cause', models.ForeignKey(on_delete=models.SET('cause not set'), to='data.Cause')),
                ('ngo_id', models.ForeignKey(on_delete=models.SET('ngo not set'), to='data.NGO')),
                ('team_member_id', models.ForeignKey(on_delete=models.SET('team member not set'), to='staff.Team_Member')),
            ],
        ),
        migrations.AddField(
            model_name='audit',
            name='consultant_id',
            field=models.ForeignKey(on_delete=models.SET('consultant not set'), to='data.Consultant'),
        ),
        migrations.AddField(
            model_name='audit',
            name='project_id',
            field=models.ForeignKey(on_delete=models.SET('project not set'), to='data.Project'),
        ),
    ]
