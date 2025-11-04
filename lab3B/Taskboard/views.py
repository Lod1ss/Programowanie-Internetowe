import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Task


def index(request):
    """Главная страница"""
    return render(request, "Taskboard/index.html")


@csrf_exempt
def tasks_list(request):
    """GET – список, POST – добавление"""
    if request.method == "GET":
        tasks = list(Task.objects.values())
        return JsonResponse(tasks, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        task = Task.objects.create(title=data["title"])
        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        })
    return None


@csrf_exempt
def task_detail(request, task_id):
    """PATCH – обновление, DELETE – удаление"""
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)

    if request.method == "PATCH":
        data = json.loads(request.body)
        task.completed = data.get("completed", task.completed)
        task.save()
        return JsonResponse({
            "id": task.id,
            "completed": task.completed
        })

    elif request.method == "DELETE":
        task.delete()
        return JsonResponse({"deleted": True})
    return None
