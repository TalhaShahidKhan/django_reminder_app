from celery import shared_task
import time
import datetime
from plyer import notification

@shared_task
def remine(slp_time,name):
    rem_time = datetime.time.fromisoformat(slp_time)
    curr_time = datetime.datetime.now().time()
    slp = datetime.datetime.combine(datetime.datetime.now(), rem_time) - datetime.datetime.combine(datetime.datetime.now(),curr_time)
    time.sleep(int(str(round(slp.total_seconds()))))
    notification.notify(
        title = 'Django Reminder App',
        message = name,
        app_icon = None,
        timeout = 5,
    )

    