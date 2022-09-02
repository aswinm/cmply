from django.contrib import admin
from performance import models


class PerformanceAdmin(admin.ModelAdmin):
    readonly_fields = ('roi', 'profit')
    list_display = ('cost', 'revenue', 'roi', 'profit')


@admin.register(models.DailyPerformance)
class DailyPerformanceAdmin(PerformanceAdmin):
    list_display = ('date', ) + PerformanceAdmin.list_display


@admin.register(models.HourlyPerformance)
class HourlyPerformance(PerformanceAdmin):
    list_display = ('datetime', ) + PerformanceAdmin.list_display
