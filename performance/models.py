from django.db import models


class PerformanceManager(models.Manager):

    def filter_by_min_roi(self, min_roi):
        return self.filter(roi__gte=min_roi)


class Performance(models.Model):

    cost = models.FloatField()
    revenue = models.FloatField()
    roi = models.FloatField(null=True, blank=True)
    profit = models.FloatField(null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)

    objects = PerformanceManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.profit = self.revenue - self.cost
        if self.cost:
            # Prevent divide by zero error
            self.roi = self.profit * 100 / self.cost
        else:
            self.roi = None
        super().save(*args, **kwargs)


class HourlyPerformance(Performance):

    datetime = models.DateTimeField()


class DailyPerformance(Performance):

    date = models.DateField()
