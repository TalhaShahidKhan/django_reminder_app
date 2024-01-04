from django.shortcuts import render,HttpResponse,redirect
from .models import Task
from .tasks import remine
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
        remine.delay(time,name)
        
        
        

        
        
        
    
    return render(request,'index.html',context)

def dlt_task(request,pk):
    task = Task.objects.get(id = pk)
    try:
        task.delete()
    except Exception as e:
        return HttpResponse(e)
    return redirect('/')



