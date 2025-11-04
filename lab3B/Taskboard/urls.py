from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/tasks/", views.tasks_list, name="tasks_list"),
    path("api/tasks/<int:task_id>/", views.task_detail, name="task_detail"),
]