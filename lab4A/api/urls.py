from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.tasks_view),
    path('tasks/<int:id>/done/', views.task_done),
    path('tasks/<int:id>/', views.task_delete),
]