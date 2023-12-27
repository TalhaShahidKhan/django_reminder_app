from django.db import models
from django.contrib.auth import get_user_model
import datetime
User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User,null = False,blank = False,on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255,null = False)
    task_dis = models.TextField(null = True,blank = True)
    task_set_time = models.DateTimeField( auto_now_add=True)
    remainder_date = models.DateField(null=True,blank = True)
    remainder_time = models.TimeField()
    def save(self, *args, **kwargs):
        if not self.remainder_date:
            self.remainder_date=datetime.datetime.now()
        
        super(Task, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.task_name