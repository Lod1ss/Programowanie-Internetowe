from django.shortcuts import render, redirect
from datetime import datetime

def home(request):
    return redirect('current_time')

def current_time(request):
    now = datetime.now()
    context = {
        "date": now.strftime("%d.%m.%Y"),  # день.месяц.год
        "time": now.strftime("%H:%M"),     # часы:минуты
    }
    return render(request, "witaj/time.html", context)