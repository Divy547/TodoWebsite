# Generated by Django 4.2.3 on 2023-09-29 20:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreateTodos',
            new_name='CreateTodo',
        ),
    ]
