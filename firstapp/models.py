from django.db import models
from datetime import datetime


class DataBeforeParsing(models.Model):
    site_name = models.CharField(max_length=50, blank=False)
    site_url = models.URLField()
    hours_shift = models.IntegerField(blank=False, null=True)
    minutes_shift = models.IntegerField(blank=False, null=True)
    seconds_shift = models.IntegerField(blank=False, null=True)

    def __str__(self):
        return self.site_name


class DataAfterParsing(models.Model):
    site_connect = models.CharField(max_length=50, blank=False, null=True)
    site_url = models.URLField(blank=True, null=True)
    site_title = models.CharField(max_length=100, blank=False, null=True)
    content_type = models.CharField(max_length=50, blank=False, null=True)
    main_heading = models.CharField(max_length=100, blank=False, null=True)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_url
