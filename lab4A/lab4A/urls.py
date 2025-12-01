from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"info": "API działa! Użyj endpointu: /api/tasks/"})

urlpatterns = [
    path("", home),
    path("api/", include("api.urls")),
]
