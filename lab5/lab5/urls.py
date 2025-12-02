from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls', namespace='books')),
    path('', RedirectView.as_view(url='/books/', permanent=False)),
]
