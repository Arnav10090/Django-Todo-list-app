from django.shortcuts import render
from todo.models import Task

# Create your views here.
def home(request):
    Tasks = Task.objects.filter(is_completed=False)
    context = {'tasks': Tasks}
    return render(request, 'home.html', context)