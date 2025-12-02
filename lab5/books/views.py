from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from django import forms

# Prosty formularz modelowy (opcjonalny — CreateView/UpdateView użyją ModelForm automatycznie,
# ale można tu doprecyzować widgety)
class BookForm(forms.ModelForm):
    publication_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 20  # opcjonalnie

    def get_queryset(self):
        qs = super().get_queryset()
        author = self.request.GET.get('author')
        if author:
            qs = qs.filter(author__icontains=author)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_filter'] = self.request.GET.get('author', '')
        return context

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:book-list')

class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('books:book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('books:book-list')
