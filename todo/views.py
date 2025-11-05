from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse


def addTasks(request):
        task = request.POST['task']
        Task.objects.create(task=task)
        return HttpResponse('This form is submitted successfully')

def markComplete(request, task_id):
        task = Task.objects.get(id=task_id)
        task.is_completed = True
        task.save()
        return redirect('home')

def markinComplete(request, task_id):
        task = Task.objects.get(id=task_id)
        task.is_completed = False
        task.save()
        return redirect('home')

def editTask(request, task_id):
        task = Task.objects.get(id=task_id)
        if request.method == 'POST':
            new_task_content = request.POST['task']
            task.task = new_task_content
            task.save()
            return redirect('home')
        else: context = {
            'task': task
        }
        return render(request, 'edit_task.html', context)

def deleteTask(request, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('home')
        
