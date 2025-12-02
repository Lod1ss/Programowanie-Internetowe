from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book-list'),
    path('add/', views.BookCreateView.as_view(), name='book-add'),
    path('<int:pk>/edit/', views.BookUpdateView.as_view(), name='book-edit'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]
