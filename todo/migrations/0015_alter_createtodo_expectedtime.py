# Generated by Django 4.2.3 on 2023-09-30 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_alter_createtodo_expecteddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createtodo',
            name='expectedTime',
            field=models.TimeField(),
        ),
    ]
