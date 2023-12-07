from django.shortcuts import render
from Task.models import TaskModel

# Create your views here.

def show_task(request):
    data = TaskModel.objects.all()

    return render(request, 'show_tasks.html', {'data': data})
