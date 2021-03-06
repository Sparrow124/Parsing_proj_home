# Generated by Django 3.2.8 on 2021-11-03 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataAfterParsing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_created=True, default=datetime.datetime.now)),
                ('site_connect', models.CharField(max_length=50, null=True)),
                ('site_url', models.URLField(blank=True, null=True)),
                ('site_title', models.CharField(max_length=100, null=True)),
                ('content_type', models.CharField(max_length=50, null=True)),
                ('main_heading', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataBeforeParsing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('site_url', models.URLField()),
                ('hours_shift', models.IntegerField(null=True)),
                ('minutes_shift', models.IntegerField(null=True)),
                ('seconds_shift', models.IntegerField(null=True)),
            ],
        ),
    ]
