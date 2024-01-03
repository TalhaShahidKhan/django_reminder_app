from django.shortcuts import render,HttpResponse,redirect
from .models import Task
import datetime
import time
# Create your views here.

def home_page(request):
    task_list = Task.objects.all()
    context = {
        'task':task_list
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        disc = request.POST.get('disc')
        # date = request.POST.get('date')
        time = request.POST.get('time')
        task = Task.objects.create(task_name=name,task_dis=disc,remainder_time=time)
        task.save()
        rem_time = datetime.time.fromisoformat(time)
        curr_time = datetime.datetime.time.
        print(type(rem_time), type(curr_time))
        slp = datetime.datetime.combine(datetime.datetime.now(), rem_time) - datetime.datetime.combine(datetime.datetime.now(),curr_time)
        print(slp)
        
        
        
    
    return render(request,'index.html',context)

def dlt_task(request,pk):
    task = Task.objects.get(id = pk)
    try:
        task.delete()
    except Exception as e:
        return HttpResponse(e)
    return redirect('/')



