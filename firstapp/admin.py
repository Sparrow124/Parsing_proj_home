from django.contrib import admin
from .models import DataBeforeParsing


class FieldForParsing(admin.ModelAdmin):
    list_display = ('site_name', 'site_url', 'hours_shift', 'minutes_shift', 'seconds_shift')
    ordering = ('seconds_shift', 'minutes_shift', 'hours_shift')


admin.site.register(DataBeforeParsing, FieldForParsing)
