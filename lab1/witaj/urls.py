from django.urls import path, include
from . import views

urlpatterns = [
    path("time/", views.current_time, name="current_time"),
    path('', views.home, name='home'),

]