# Generated by Django 3.2.8 on 2021-10-30 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databeforeparsing',
            name='hours_shift',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='databeforeparsing',
            name='minutes_shift',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='databeforeparsing',
            name='seconds_shift',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
