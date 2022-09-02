import random
from django.core.management.base import BaseCommand
from performance import models


class Command(BaseCommand):
    help = 'Random Revenue generation'

    def handle(self, *args, **options):
        daily_performances = models.DailyPerformance.objects.filter_by_min_roi(min_roi=0.5)
        count = daily_performances.count()
        print(f"Total records in queryset: {count}")
        print(f"Total records multiplied by 2: {count * 2}")
        for index, performance in enumerate(daily_performances, start=1):
            print(f"Processing record {index}/{count}")
            multiplier = random.uniform(0.5, 2)
            performance.revenue *= multiplier
            performance.save()
