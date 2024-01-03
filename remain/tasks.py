from celery import shared_task
import time
import datetime

@shared_task
def remine(time):
    rem_time = datetime.time.fromisoformat(time)
    curr_time = datetime.datetime.now().strftime("%H:%M")
    slp = rem_time - curr_time
    print(slp)
    