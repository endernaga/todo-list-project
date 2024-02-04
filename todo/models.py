import datetime

from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    date = models.DateTimeField(default=datetime.date.today)
    finished = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tags, related_name='tasks')

    def __str__(self):
        return self.content
