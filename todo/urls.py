from django.urls import path
from . import views

urlpatterns = [
    path('addTasks/', views.addTasks, name='addTasks'),
    path('markComplete/<int:task_id>/', views.markComplete, name='markComplete'),
    path('markinComplete/<int:task_id>/', views.markinComplete, name='markinComplete'),
    path('editTask/<int:task_id>/', views.editTask, name='editTask'),
    path('deleteTask/<int:task_id>/', views.deleteTask, name='deleteTask'),
]