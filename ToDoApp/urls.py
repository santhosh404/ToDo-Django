from django.urls import path
from . import views


urlpatterns = [
        path('app', views.index, name = 'index'),
        path('tasks', views.tasks, name = 'tasks'),
        path('delete/<int:todo_id>/', views.delete, name = 'delete')
]