from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


def validate_publication_year(value):
    if value.year > 2025:
        raise ValidationError("Rok wydania nie może być późniejszy niż 2025.")


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField(validators=[validate_publication_year])

    class Meta:
        ordering = ['-publication_date', 'title']

    def __str__(self):
        return f"{self.title} — {self.author} ({self.publication_date})"

    def get_absolute_url(self):
        return reverse('books:book-list')
