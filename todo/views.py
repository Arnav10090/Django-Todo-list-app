from django.shortcuts import render
from .models import Task
from django.http import HttpResponse

def addTasks(request):
        task = request.POST['task']
        Task.objects.create(task=task)
        return HttpResponse('This form is submitted successfully')
        
