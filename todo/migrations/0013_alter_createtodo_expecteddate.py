# Generated by Django 4.2.3 on 2023-09-29 23:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_createtodo_expecteddate_createtodo_expectedtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createtodo',
            name='expectedDate',
            field=models.DateField(default=datetime.date(2000, 3, 1)),
        ),
    ]
