# Generated by Django 4.2.3 on 2023-09-29 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_rename_createtodos_createtodo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createtodo',
            name='todo',
        ),
        migrations.AddField(
            model_name='createtodo',
            name='desc',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='createtodo',
            name='expectedDate',
            field=models.DateField(auto_now_add = True),
        ),
        migrations.AddField(
            model_name='createtodo',
            name='expectedTime',
            field=models.TimeField(auto_now_add = True),
        ),
        migrations.AlterField(
            model_name='createtodo',
            name='title',
            field=models.CharField(default='', max_length=10),
        ),
    ]
