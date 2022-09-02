import time
from cmply.celery import app
from performance import models


@app.task
def slow_iteration():
    daily_performances = models.DailyPerformance.objects.all()[:50]
    for index, performance in enumerate(daily_performances, start=1):
        print(f"Processing record: {index}")
        time.sleep(6)
