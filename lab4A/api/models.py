from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)   # ustawiana przy utworzeniu
    updated = models.DateTimeField(auto_now=True)       # ustawiana przy każdej zmianie

    def __str__(self):
        return self.title
