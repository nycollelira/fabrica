# Generated by Django 4.2.4 on 2023-09-02 19:53

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0002_rename_complete_task_completo_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Tarefas',
        ),
    ]
