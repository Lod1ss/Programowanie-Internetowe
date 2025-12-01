from django.db import migrations

def add_sample_tasks(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')
    Task.objects.create(title="Kupić mleko", done=False)
    Task.objects.create(title="Kupić mięso", done=False)

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(add_sample_tasks),
    ]
