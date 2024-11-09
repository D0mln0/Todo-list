from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=255)