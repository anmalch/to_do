from django.db import models

from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)


class Todo(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    created_data = models.DateTimeField
    updated_data = models.DateTimeField
    author = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    status = models.BooleanField
