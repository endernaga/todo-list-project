# Generated by Django 5.0.1 on 2024-02-04 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]