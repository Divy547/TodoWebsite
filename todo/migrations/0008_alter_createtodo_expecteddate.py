# Generated by Django 4.2.3 on 2023-09-29 23:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_createtodo_expecteddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createtodo',
            name='expectedDate',
            field=models.DateField(default=datetime.date(2023, 9, 30)),
        ),
    ]