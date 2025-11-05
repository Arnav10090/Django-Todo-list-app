from django.shortcuts import render
from todo.models import Task

# Create your views here.
def home(request):
    Tasks = Task.objects.filter(is_completed=False).order_by('-updated_at') # for descending order of data in frontend
    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')

    context = {
        'tasks': Tasks, 
        'completed_tasks': completed_tasks,
        }
    return render(request, 'home.html', context)