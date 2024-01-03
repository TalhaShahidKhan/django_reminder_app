from celery import shared_task
import time
import datetime

@shared_task
def remine(date,time):
    rem_date = datetime.date.fromisoformat(date)
    rem_time = datetime.time.fromisoformat(time)
    