from django.shortcuts import render
from django.http import JsonResponse
from .models import Visit

def index(request):
    visit, created = Visit.objects.get_or_create(id=1)
    visit.count += 1
    visit.save()
    return render(request, "Visitcounter/counter.html", {"visit_count": visit.count})

def increment_counter(request):
    if request.method == "POST":
        visit, _ = Visit.objects.get_or_create(id=1)
        visit.count += 1
        visit.save()
        return JsonResponse({"count": visit.count})
    return JsonResponse({"error": "Invalid request"}, status=400)
