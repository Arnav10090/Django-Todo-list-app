from django.urls import path
from . import views

urlpatterns = [
    path('addTasks/', views.addTasks, name='addTasks'),
]