# Generated by Django 3.2.8 on 2021-11-03 09:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_alter_dataafterparsing_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataafterparsing',
            name='date_create',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime.now),
        ),
    ]
