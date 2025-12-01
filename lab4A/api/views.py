from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task
import json

@csrf_exempt
def tasks_view(request):
    if request.method == "GET":
        data = list(Task.objects.values())
        return JsonResponse({"tasks": data})

    if request.method == "POST":
        body = json.loads(request.body)
        t = Task.objects.create(title=body["title"])
        return JsonResponse({"id": t.id, "title": t.title, "done": t.done}, status=201)


@csrf_exempt
def task_done(request, id):
    if request.method == "PATCH":
        Task.objects.filter(id=id).update(done=True)
        return JsonResponse({"id": id, "done": True})


@csrf_exempt
def task_delete(request, id):
    if request.method == "DELETE":
        Task.objects.filter(id=id).delete()
        return JsonResponse({"deleted": True})